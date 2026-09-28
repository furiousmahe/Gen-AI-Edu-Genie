import os
import traceback
from google import genai

def get_learning_recommendations(topic: str) -> str:
    prompt = f"""
You are an AI tutor. The student wants to learn about: {topic}.
Suggest a structured and adaptive learning path including key topics, order of learning, and resources.
Include beginner, intermediate, and advanced levels if needed.
"""
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-1.5-pro",
            contents=prompt
        )
        print("🧠 Gemini raw response:", response)

        if hasattr(response, "text") and response.text:
            return response.text
        else:
            return "❌ Could not extract content from Gemini response."
    except Exception as e:
        traceback.print_exc()
        return f"❌ Error occurred: {str(e)}"