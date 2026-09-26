import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.config import DB_DIR, DOCS_DIR, EMBEDDING_MODEL, EMBEDDING_DEVICE, CHUNK_SIZE, CHUNK_OVERLAP

class VectorStoreManager:
    def __init__(self):
        """Vektör veritabanını ve yerleştirme (embedding) modelini başlatır."""
        print("Veritabanı yöneticisi başlatılıyor...")
        
        # SİHİRLİ DOKUNUŞ: Sadece İngilizce değil, Türkçe de anlayan çok dilli arama motoru
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2", 
            model_kwargs={'device': EMBEDDING_DEVICE}
        )
        
        self.db = Chroma(persist_directory=DB_DIR, embedding_function=self.embeddings)
        
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE, 
            chunk_overlap=CHUNK_OVERLAP
        )

    def process_and_add_document(self, file_path, filename):
        """Verilen dosyayı okur, parçalar ve vektör veritabanına KALICI OLARAK ekler."""
        if filename.endswith(".pdf"):
            loader = PyPDFLoader(file_path)
        elif filename.endswith(".txt") or filename.endswith(".md"):
            loader = TextLoader(file_path, encoding="utf-8")
        else:
            raise ValueError("Sadece PDF, TXT veya MD formatları desteklenmektedir.")
            
        docs = loader.load()
        chunks = self.text_splitter.split_documents(docs)
        
        # Metin parçalarını (chunks) geçici hafızaya (RAM) ekle
        self.db.add_documents(chunks)
        
        # İŞTE HAYAT KURTARAN SATIR: Öğrenilenleri Hard-Diske (chroma_db) Kalıcı Olarak Kaydet!
        self.db.persist()
        
        return True

    def search_context(self, user_query, k=10):
        """Sorguya en uygun metin parçalarını ve kaynaklarını bulur."""
        if not self.db:
            return "Veritabanı bulunamadı."
            
        # Arama ufkunu 3'ten 10'a çıkardık! Artık dosyanın çok daha büyük bir kısmını görecek.
        results = self.db.similarity_search(user_query, k=k)
        
        context = ""
        import os
        
        for doc in results:
            source_path = doc.metadata.get("source", "Bilinmeyen_Kaynak")
            filename = os.path.basename(source_path)
            context += f"[KAYNAK: {filename}]\n{doc.page_content}\n\n"
            
        return context