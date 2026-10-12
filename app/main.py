from fastapi import FastAPI
from app.api.v1_endpoints import router as api_router

app = FastAPI(
    title="DocuMind AI API",
    description="Gemini Pro destekli doküman analiz ve soru-cevap platformu",
    version="0.1.0"
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "DocuMind API is running"}
