
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("ERROR: Gemini API key was not found in .env")
    raise SystemExit(1)

print("Connecting to Gemini...")

try:
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents="Reply with only these words: Gemini is working",
        config={
            "max_output_tokens": 30,
            "http_options": {"timeout": 60000},
        },
    )

    print("SUCCESS!")
    print(response.text)

except Exception as error:
    print("FAILED!")
    print(type(error).__name__)
    print(str(error))
