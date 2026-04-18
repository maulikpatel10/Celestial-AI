from fastapi import APIRouter
from app.services.rag_service import query_pdf
from app.services.llm_service import generate_ai_response
router = APIRouter()

# 🔥 MEMORY STORE
chat_memory = []

@router.post("/chat")
async def chat_api(user_input: str):
    try:
        global chat_memory

        # 1️⃣ Save user message
        chat_memory.append({
            "role": "user",
            "content": user_input
        })

        # 2️⃣ Get PDF context
        context = query_pdf(user_input)

        # 🔥 Only use PDF if valid
        if context is not None and len(context.strip()) > 30:
            context_text = context[:5000]  # Increased size limit to prevent destroying answers
        else:
            context_text = None

        # 3️⃣ Generate AI response (GPT 🔥)
        response = generate_ai_response(user_input, chat_memory, context_text)

        # 4️⃣ Save AI response
        chat_memory.append({
            "role": "assistant",
            "content": response
        })

        # 🔥 Prevent very large responses (avoid crash)
        response = response[:1000]

        return {"response": response}

    except Exception as e:
        return {"response": "Error: " + str(e)}