import os
from google import genai

def explain_topic(topic: str) -> str:
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        client = genai.Client(api_key=api_key)

        prompt = f"Explain the concept of '{topic}' in a simple and clear way for a school student."
        response = client.models.generate_content(
            model="gemini-1.5-pro",
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error in Explanation: {e}"