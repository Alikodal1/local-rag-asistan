import os
from src.vector_store import VectorStoreManager

def init_database():
    print("Veritabanı başlatılıyor ve klasör taranıyor...")
    vector_store = VectorStoreManager()
    
    # Klasör yolunu belirliyoruz
    icerik_klasoru = os.path.join("docs", "icerik")
    
    if not os.path.exists(icerik_klasoru):
        print(f"HATA: '{icerik_klasoru}' klasörü bulunamadı!")
        return

    basarili = 0
    # Klasördeki tüm dosyaları tara
    for dosya_adi in os.listdir(icerik_klasoru):
        if dosya_adi.endswith((".md", ".txt", ".pdf")):
            dosya_yolu = os.path.join(icerik_klasoru, dosya_adi)
            try:
                print(f"Öğreniliyor: {dosya_adi}...")
                vector_store.process_and_add_document(dosya_yolu, dosya_adi)
                basarili += 1
            except Exception as e:
                print(f"Hata ({dosya_adi}): {e}")
                
    print(f"\nİşlem tamam! Toplam {basarili} belge başarıyla kalıcı hafızaya (ChromaDB) kazındı.")

if __name__ == "__main__":
    init_database()