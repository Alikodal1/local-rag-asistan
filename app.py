import os
from flask import Flask, request, Response, render_template, jsonify

# Yazdığımız kendi modüllerimizi (Sınıfları) içeri aktarıyoruz
from src.config import DOCS_DIR
from src.vector_store import VectorStoreManager
from src.llm_chain import LLMManager
from flask import Flask, request, jsonify, render_template, Response, stream_with_context

# Flask uygulamasını başlat ("templates" klasörünü otomatik tanıyacak)
app = Flask(__name__)

# Sistem Yöneticilerini (Sınıf Örneklerini) Başlat
vector_store = VectorStoreManager()
llm_manager = LLMManager()  # Burada llm_manager adıyla başlattık

@app.route("/")
def index():
    """Ön yüzü (HTML) kullanıcıya sunar."""
    return render_template("index.html")

@app.route("/api/upload", methods=["POST"])
def upload_file():
    """Arayüzden gelen dosyayı alır ve Vektör Veritabanı Yöneticisine iletir."""
    if 'file' not in request.files or request.files['file'].filename == '':
        return jsonify({"error": "Geçerli bir dosya bulunamadı"}), 400
        
    file = request.files['file']
    
    if not os.path.exists(DOCS_DIR):
        os.makedirs(DOCS_DIR)
        
    file_path = os.path.join(DOCS_DIR, file.filename)
    file.save(file_path)
    
    try:
        vector_store.process_and_add_document(file_path, file.filename)
        return jsonify({"message": f"'{file.filename}' başarıyla öğrenildi!"}), 200
    except Exception as e:
        import traceback
        print(f"\n--- DOSYA YÜKLEME HATASI ---\n{traceback.format_exc()}\n----------------------------\n")
        return jsonify({"error": f"Dosya işlenirken hata oluştu: {str(e)}"}), 500

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json
    user_query = data.get("query", "")
    
    # 1. Bağlamı çek
    context = vector_store.search_context(user_query, k=4)
    
    # 2. Kaynakları önceden hazırla ve metin olarak tut
    import re
    kaynaklar = set(re.findall(r"\[KAYNAK: (.*?)\]", context))
    kaynak_metni = ""
    
    if kaynaklar:
        kaynak_metni += "\n\n**📚 Kullanılan Kaynaklar:**\n"
        for kaynak in kaynaklar:
            kaynak_metni += f"- {kaynak}\n"

    # 3. Akışkan jeneratör fonksiyonu
    # 3. Akışkan jeneratör fonksiyonu
    def generate():
        tam_cevap = "" # Yapay zekanın cevabını hafızada tutmak için
        
        # Önce yapay zekanın cevabını kelime kelime akıt
        for chunk in llm_manager.generate_response_stream(context, user_query):
            tam_cevap += chunk # Gelen her kelimeyi birleştir
            yield chunk
        
        # Yapay zekanın konuşması bitti! Eğer "bulamadım" DEMEDİYSE kaynakları yapıştır
        if kaynak_metni and "bulamadım" not in tam_cevap.lower():
            yield kaynak_metni

    # Cevabı parça parça (text/plain) olarak arayüze fırlat
    return Response(stream_with_context(generate()), mimetype='text/plain')

# Çalıştırma bloğu KESİNLİKLE en solda (girintisiz) olmalıdır!
if __name__ == "__main__":
    app.run(debug=False, port=5000)
    