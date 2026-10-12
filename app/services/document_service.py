import io
from pypdf import PdfReader
from fastapi import UploadFile, HTTPException

class DocumentService:
    @staticmethod
    async def extract_text(file: UploadFile) -> str:
        content = await file.read()
        filename = file.filename.lower()

        if filename.endswith(".txt"):
            try:
                return content.decode("utf-8")
            except UnicodeDecodeError:
                return content.decode("latin-1")

        elif filename.endswith(".pdf"):
            try:
                pdf_reader = PdfReader(io.BytesIO(content))
                extracted_text = []
                for page_num, page in enumerate(pdf_reader.pages):
                    text = page.extract_text()
                    if text:
                        extracted_text.append(f"--- Sayfa {page_num + 1} ---\n{text}")
                
                full_text = "\n\n".join(extracted_text)
                if not full_text.strip():
                    raise HTTPException(status_code=400, detail="PDF dosyasından okunabilir metin çıkarılamadı.")
                return full_text
            except Exception as e:
                raise HTTPException(status_code=400, detail=f"PDF işlenirken hata oluştu: {str(e)}")

        else:
            raise HTTPException(status_code=400, detail="Yalnızca .pdf ve .txt uzantılı dosyalar desteklenmektedir.")

document_service = DocumentService()
