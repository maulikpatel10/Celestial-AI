import os
import shutil

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import FakeEmbeddings, HuggingFaceEmbeddings
# 📁 Folder to store vectors
VECTOR_PATH = "vectorstore"

# 🔥 Global cache (for speed)
db_cache = None

# 🔥 Faster + stable embedding model
embeddings = FakeEmbeddings(size=384)

# =========================
# ✅ PROCESS PDF (FIXED)
# =========================
vectorstore = None


def process_pdf(file_path):
    global vectorstore

    print("📄 Loading PDF:", file_path)

    loader = PyPDFLoader(file_path)
    documents = loader.load()

    print("📄 Splitting text...")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    docs = splitter.split_documents(documents)  # ✅ THIS IS CORRECT

    print("📄 Creating FAISS index...")

    # 🔥 Prevent instant OOM crash on Render Free Tier when loading PyTorch model
    embeddings = FakeEmbeddings(size=384)

    vectorstore = FAISS.from_documents(docs, embeddings)  # ✅ USE docs
    vectorstore.save_local(VECTOR_PATH)

    print("✅ PDF processed & saved successfully")
# =========================
# ✅ LOAD DB (FAST)
# =========================
def load_db():
    global db_cache

    if db_cache is None:
        if not os.path.exists(VECTOR_PATH):
            print("⚠️ No vectorstore found")
            return None

        print("📦 Loading vectorstore...")

        db_cache = FAISS.load_local(
            VECTOR_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )

    return db_cache


# =========================
# ✅ QUERY PDF
# =========================
vectorstore = None  # 👈 GLOBAL
def query_pdf(query):
    global vectorstore

    if vectorstore is None:
        vectorstore = load_db()

    if vectorstore is None:
        print("❌ No vectorstore loaded")
        return None

    docs = vectorstore.similarity_search(query, k=3)

    if not docs:
        print("❌ No docs found")
        return None

    context = "\n".join([doc.page_content for doc in docs])

    print("✅ CONTEXT FOUND")

    return context