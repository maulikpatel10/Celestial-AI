import os

from pypdf import PdfReader

# 🔥 Store the raw PDF text in memory directly to bypass FAISS segfaults completely
pdf_text_cache = ""

# =========================
# ✅ PROCESS PDF (ULTRA-SAFE)
# =========================
def process_pdf(file_path):
    global pdf_text_cache

    print("📄 Loading PDF:", file_path)

    try:
        reader = PdfReader(file_path)
        
        # OOM Safeguard: Limit massive PDF uploads on Render Free Tier
        max_pages = min(15, len(reader.pages))
        extracted_text = ""
        
        for i in range(max_pages):
            page_text = reader.pages[i].extract_text()
            if page_text:
                extracted_text += page_text + "\n\n"
        
        pdf_text_cache = extracted_text
        print("✅ PDF processed & extracted successfully. Text length:", len(pdf_text_cache))
    except Exception as e:
        print("❌ Failed to process PDF:", e)

# =========================
# ✅ QUERY PDF
# =========================
def query_pdf(query):
    global pdf_text_cache

    if not pdf_text_cache:
        print("❌ No PDF loaded into memory")
        return None

    print("✅ Returning PDF context (bypassing FAISS)")
    return pdf_text_cache