from fastapi import APIRouter, UploadFile, File
import os

from app.services.rag_service import process_pdf

router = APIRouter()

UPLOAD_DIR = "uploads"

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        if not os.path.exists(UPLOAD_DIR):
            os.makedirs(UPLOAD_DIR)

        file_path = os.path.join(UPLOAD_DIR, file.filename)

        # Save file
        with open(file_path, "wb") as f:
            f.write(await file.read())

        print("✅ PDF Saved at:", file_path)

        # Process PDF
        process_pdf(file_path)
        
        # Clear legacy memory to avoid AI getting confused across different PDFs
        from app.routes.chat import chat_memory
        chat_memory.clear()

        print("✅ PDF Processed & Memory Wiped")

        return {"message": "PDF uploaded successfully"}

    except Exception as e:
        print("UPLOAD ERROR:", e)
        return {"message": "Upload failed: " + str(e)}