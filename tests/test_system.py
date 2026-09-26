import unittest
import os
import sys

# src modülünü bulabilmesi için ana dizini path'e ekliyoruz
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.config import DOCS_DIR, DB_DIR
from src.vector_store import VectorStoreManager

class TestRAGSystem(unittest.TestCase):
    def setUp(self):
        """Her testten önce çalışacak ön hazırlık (Setup) adımı"""
        if not os.path.exists(DOCS_DIR):
            os.makedirs(DOCS_DIR)
        self.vector_store = VectorStoreManager()

    def test_config_paths(self):
        """Konfigürasyon yollarının doğru ayarlandığını test eder"""
        self.assertTrue(DOCS_DIR.endswith("icerik"), "Doküman klasör yolu hatalı!")
        self.assertTrue(DB_DIR.endswith("chroma_db"), "Veritabanı klasör yolu hatalı!")

    def test_vector_store_initialization(self):
        """Vektör veritabanı sınıfının doğru başlatıldığını (Initialize) test eder"""
        self.assertIsNotNone(self.vector_store.embeddings, "Embedding modeli yüklenemedi!")
        self.assertIsNotNone(self.vector_store.db, "Chroma veritabanı başlatılamadı!")
        self.assertIsNotNone(self.vector_store.text_splitter, "Metin parçalayıcı yüklenemedi!")

if __name__ == '__main__':
    unittest.main()