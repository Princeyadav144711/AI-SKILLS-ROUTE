
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY is missing from .env file.")

client = genai.Client(api_key=API_KEY)


def ask_gemini(prompt):
    try:
        print("Connecting to Gemini 3.8 Flash...")

        interaction = client.interactions.create(
            model="gemini-3.8-flash",
            input=prompt,
            timeout=180
        )

        print("Gemini response received!")

        return interaction.output_text or "Empty response from Gemini."

    except Exception as e:
        print("Gemini API Error:", repr(e))
        return "Gemini API error: " + str(e)
