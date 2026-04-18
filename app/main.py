from fastapi import FastAPI
from app.routes import chat, upload

app = FastAPI()

@app.api_route("/", methods=["GET", "HEAD"])
def root():
    return {"message": "API is running 🚀"}

app.include_router(chat.router)
app.include_router(upload.router)

if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
