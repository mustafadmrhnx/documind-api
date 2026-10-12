import google.generativeai as genai
from app.core.config import settings

class GeminiService:
    def __init__(self):
        if settings.GEMINI_API_KEY:
            genai.configure(api_key=settings.GEMINI_API_KEY)
            self.model = genai.GenerativeModel("gemini-1.5-flash")
        else:
            self.model = None

    async def generate_response(self, prompt: str, context: str = "") -> str:
        if not self.model:
            return "Hata: GEMINI_API_KEY tanımlanmamış."
        
        full_prompt = f"Bağlam:\n{context}\n\nKullanıcı Sorusu: {prompt}" if context else prompt
        response = self.model.generate_content(full_prompt)
        return response.text

gemini_service = GeminiService()
