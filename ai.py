from google import genai
from config  import gen_ai

client = genai.Client(api_key=gen_ai)

def ask_ai(question):
    try:
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents=question
        )
        return response.text
    
    except Exception as e:
        return f"Sorry, an error occurred: {e}"