import os
from google import genai

def answer_question_with_gemini(question: str) -> str:
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        client = genai.Client(api_key=api_key)
        
        response = client.models.generate_content(
            model="gemini-1.5-pro",
            contents=question
        )
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error in QnA: {e}"