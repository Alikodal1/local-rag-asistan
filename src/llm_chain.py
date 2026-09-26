from langchain_ollama import OllamaLLM
from src.config import LLM_MODEL, LLM_TEMPERATURE, LLM_REPEAT_PENALTY

class LLMManager:
    def __init__(self):
        """Yapay Zeka (LLM) motorunu belirtilen ayarlarla başlatır."""
        print(f"Yapay Zeka motoru ({LLM_MODEL}) başlatılıyor...")
        self.llm = OllamaLLM(
            model=LLM_MODEL,
            temperature=LLM_TEMPERATURE,
            repeat_penalty=LLM_REPEAT_PENALTY
        )

    def create_prompt(self, context, query):
        return f"""Sen uzman bir mühendislik asistanısın.
Görevin, aşağıdaki BAĞLAM metnindeki bilgileri kullanarak kullanıcının sorusuna doğal, akıcı ve kurallı bir Türkçe ile yanıt vermektir.

Rehber:
- Sadece bağlamda verilen gerçeklere sadık kal.
- Cümlelerini kısa, mantıklı ve anlaşılır kur. Kelime uydurmaktan kaçın.
- Bilgileri özetleyerek, tekrara düşmeden doğrudan aktar.
- Eğer sorunun cevabı bağlamda yoksa, sadece "Üzgünüm, belgelerde bu sorunun cevabını bulamadım." de.

BAĞLAM:
{context}

SORU: {query}
CEVAP:"""

    def generate_response(self, context, query):
        """Modelden tam cevabı tek seferde (senkron) alır."""
        prompt = self.create_prompt(context, query)
        return self.llm.invoke(prompt)

    def generate_response_stream(self, context, query):
        """LLM'in ürettiği cevabı kelime kelime (stream) döndürür."""
        prompt = self.create_prompt(context, query)
        
        # .stream() metodu sayesinde model kelimeleri ürettikçe anında gönderir
        for chunk in self.llm.stream(prompt):
            # Model tipine göre (String veya Obje) metni güvenli şekilde ayıkla
            yield chunk.content if hasattr(chunk, "content") else chunk