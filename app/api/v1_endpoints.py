from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from pydantic import BaseModel
from app.services.gemini_service import gemini_service
from app.services.document_service import document_service

router = APIRouter()

class AskRequest(BaseModel):
    prompt: str
    context: str = ""

class AskResponse(BaseModel):
    answer: str

@router.post("/ask", response_model=AskResponse)
async def ask_gemini(payload: AskRequest):
    answer = await gemini_service.generate_response(payload.prompt, payload.context)
    return AskResponse(answer=answer)

@router.post("/documents/analyze")
async def analyze_document(
    file: UploadFile = File(...),
    prompt: str = Form("Bu dokümanın temel noktalarını özetle ve ana çıkarımları listele.")
):
    extracted_text = await document_service.extract_text(file)
    ai_response = await gemini_service.generate_response(prompt=prompt, context=extracted_text)
    
    return {
        "filename": file.filename,
        "character_count": len(extracted_text),
        "prompt": prompt,
        "analysis": ai_response
    }
