from fastapi import FastAPI
from app.routes import chat, upload

app = FastAPI()

# include routes
app.include_router(chat.router)
app.include_router(upload.router)

@app.get("/")
def root():
    return {"message": "API is running 🚀"}

# 🔥 IMPORTANT FOR RENDER
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)