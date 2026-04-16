from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_ai_response(user_input, history, context=None):
    try:
        messages = []

        messages.append({
            "role": "system",
            "content": "You are a smart AI assistant. Give helpful answers."
        })

        for msg in history[-6:]:
            messages.append(msg)

        if context:
            messages.append({
                "role": "system",
                "content": f"The user has uploaded a PDF document. Here is the exact extracted text from the PDF: \n\n{context}\n\nPlease use this information to answer any questions about the PDF directly as if you have read it."
            })

        messages.append({
            "role": "user",
            "content": user_input
        })

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # ✅ FIXED MODEL
            messages=messages,
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        return "❌ Error: " + str(e)