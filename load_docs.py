import os
from src.config import DOCS_DIR
from src.vector_store import VectorStoreManager

print("Veritabanı yöneticisi başlatılıyor...")
vs = VectorStoreManager()

print(f"\n'{DOCS_DIR}' klasöründeki dosyalar taranıyor...")
for filename in os.listdir(DOCS_DIR):
    if filename.endswith(".md") or filename.endswith(".txt") or filename.endswith(".pdf"):
        file_path = os.path.join(DOCS_DIR, filename)
        print(f"-> Öğreniliyor: {filename}")
        try:
            vs.process_and_add_document(file_path, filename)
            print(f"   [BAŞARILI] {filename} veritabanına eklendi.")
        except Exception as e:
            print(f"   [HATA] {filename} işlenemedi: {str(e)}")

print("\nBütün belgeler başarıyla vektör veritabanına (ChromaDB) aktarıldı!")