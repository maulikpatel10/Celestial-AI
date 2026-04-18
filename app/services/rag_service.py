import os

from langchain_community.document_loaders import PyPDFLoader

# 🔥 Store the raw PDF text in memory directly to bypass FAISS segfaults completely
pdf_text_cache = ""

# =========================
# ✅ PROCESS PDF (ULTRA-SAFE)
# =========================
def process_pdf(file_path):
    global pdf_text_cache

    print("📄 Loading PDF:", file_path)

    try:
        loader = PyPDFLoader(file_path)
        documents = loader.load()
        
        # Simply append all text together
        pdf_text_cache = "\n\n".join([doc.page_content for doc in documents])
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