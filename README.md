# 🧠 Yerel RAG (Retrieval-Augmented Generation) Yapay Zeka Asistanı

Bu proje, tamamen **çevrimdışı (lokal)** çalışan, veri gizliliğini %100 koruyan ve kendi yüklediğiniz PDF/Markdown belgeleri üzerinden soruları yanıtlayabilen bir yapay zeka asistanıdır. 

Geleneksel LLM'lerin aksine, bu sistem RAG mimarisi kullanarak halüsinasyonları (uydurma bilgileri) en aza indirir, sadece verdiğiniz belgelere sadık kalır ve kullandığı kaynakları yanıtın sonunda belirtir. Üstelik ChatGPT benzeri **Streaming (Akışkan)** veri transferi ile kelimeleri ekrana anında döker.

---

## ✨ Öne Çıkan Özellikler

- **%100 Yerel ve Gizli:** Verileriniz asla internete veya üçüncü parti sunuculara (OpenAI, Google vb.) gönderilmez. Tüm işlemler kendi donanımınızda gerçekleşir.
- **Akışkan Yanıt Sistemi (Streaming API):** Cevapları bekletmek yerine daktilo efektiyle ekrana anında yansıtır.
- **Kaynak Gösterimi (Citation):** Yapay zeka cevap verirken arka planda hangi metinleri okuduğunu analiz eder ve cevabın altına kaynakçasını ekler.
- **Gelişmiş Prompt Mühendisliği:** Sistemin konuları birbirine karıştırmasını ve alakasız sorulara uydurma cevaplar vermesini engelleyen katı kural setleri içerir.
- **Çok Dilli (Multilingual) Arama:** Türkçe dilini kusursuz anlayan vektör arama motoru (`paraphrase-multilingual-MiniLM-L12-v2`) sayesinde bağlamları hatasız eşleştirir.
- **Sürükle-Bırak Desteği:** Kullanıcı arayüzü üzerinden anında yeni belge (PDF/TXT/MD) yükleme ve veritabanını dinamik olarak güncelleme yeteneği.

---

## 📂 Proje Dosya Yapısı ve Mimari

Proje, Sürdürülebilirlik (Maintainability) ilkelerine uygun olarak modüler bir yapıda tasarlanmıştır:

```text
local-rag-asistan/
│
├── chroma_db/              # Vektör veritabanının fiziksel olarak kaydedildiği klasör.
├── docs/icerik/            # RAG sistemine beslenecek başlangıç belgeleri.         
│   ├── muhendislik.md      
│   ├── python.md           
│   └── yapayzeka.md        
├── src/                    # Ana çalışma mantığını (config, vector_store, llm_chain) içeren kaynak klasörü.
├── templates/              
│   └── index.html          # Kullanıcı arayüzü (Frontend - Streaming ve sürükle-bırak destekli).
├── tests/                  # Proje test dosyalarının bulunduğu klasör.
│   └── test_system.py      # Sistemin entegrasyon ve birim testleri.
├── venv/                   # Python sanal ortamı (Git'e yüklenmez).
├── .gitignore              # Git'e yüklenmemesi gereken geçici veya büyük dosyaların listesi.
├── app.py                  # Uygulamanın kalbi, Flask sunucusu ve API uç noktaları.
├── init_db.py              # Belgeleri okuyup vektör veritabanını sıfırdan oluşturan dosya.
├── load_docs.py            # Yeni belgeleri veritabanına dinamik yüklemek/güncellemek için yardımcı script.
├── README.md               # Proje tanıtım ve dökümantasyon dosyası.
└── requirements.txt        # Projenin çalışması için gereken Python kütüphaneleri.


## ⚙️ Kurulum ve Çalıştırma

Bu projeyi bilgisayarınızda çalıştırmak için aşağıdaki adımları sırasıyla uygulayın.

### 1. Ön Hazırlık
Sistemi kurmadan önce bilgisayarınızda Python (3.10+) ve Ollama'nın yüklü olduğundan emin olun.

Ollama'yı kurduktan sonra bilgisayarınızda bir terminal açıp kullanacağımız yapay zeka modelini indirin ve başlatın:

-ollama run qwen2.5:3b

###2. Projeyi Kurma ve Başlatma
Yeni bir terminal penceresi açın ve projeyi ayağa kaldırmak için aşağıdaki komutları sırasıyla çalıştırın:


# 1. Proje klasörünün içine girin
cd local-rag-asistan

# 2. İzole bir Python sanal ortamı (virtual environment) oluşturun
python -m venv venv

# 3. Sanal ortamı aktif edin (Windows için)
venv\Scripts\activate
# (Mac/Linux kullanıyorsanız şu komutu girin: source venv/bin/activate)

# 4. Projenin çalışması için gerekli kütüphaneleri yükleyin
pip install -r requirements.txt

# 5. 'docs/icerik' klasöründeki belgelerinizi taratıp Vektör Veritabanını oluşturun
python init_db.py

# 6. Uygulamayı (Web sunucusunu) başlatın
python app.py


