from fastapi import FastAPI
from app.routes import chat, upload

app = FastAPI()

# ✅ include routes
app.include_router(chat.router)
app.include_router(upload.router)

@app.get("/")
def root():
    return {"message": "API is running 🚀"}