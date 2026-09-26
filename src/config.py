import os

# Temel Dizin Ayarları
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_DIR = os.path.join(BASE_DIR, "chroma_db")
DOCS_DIR = os.path.join(BASE_DIR, "docs", "icerik")

# Yapay Zeka Model Ayarları
LLM_MODEL = "qwen2.5:3b" 
LLM_TEMPERATURE = 0.3
LLM_REPEAT_PENALTY = 1.2

# Vektör (Embedding) Ayarları
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
EMBEDDING_DEVICE = "cpu"

# Metin Parçalama (Chunking) Ayarları
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200