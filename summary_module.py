import os
from google import genai

def summarize_text(text: str) -> str:
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        client = genai.Client(api_key=api_key)

        prompt = f"Summarize the following text in simple language:\n\n{text}"
        response = client.models.generate_content(
            model="gemini-1.5-pro",
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error in Summary: {e}"