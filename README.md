
# DocuMind AI API 🚀

DocuMind, Google Gemini 1.5 Flash destekli, asenkron PDF ve doküman analizi yapan kurumsal mimarili bir RESTful API servisidir.

## 🛠️ Mimari & Teknolojiler
- **Dil & Framework**: Python 3.12, FastAPI
- **Yapay Zekâ**: Google Generative AI (Gemini 1.5 Flash)
- **Mimari**: Katmanlı Mimari (Clean / Layered Architecture)
- **Konteynerleştirme**: Docker & Docker Compose
- **Dokümantasyon**: OpenAPI / Swagger UI

## 📂 Klasör Yapısı
```text
documind-api/
├── app/
│   ├── api/          # HTTP Endpoint yönlendirmeleri
│   ├── core/         # Konfigürasyon ve ortam değişkenleri (.env)
│   ├── services/     # Gemini ve PDF iş mantığı (business logic)
│   └── main.py       # FastAPI uygulama giriş noktası
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md