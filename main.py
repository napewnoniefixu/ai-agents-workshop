import os
from dotenv import load_dotenv
from google import genai
from utils import print_token_usage

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
model = "gemini-2.5-flash"

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model=model,
    contents="Explain how AI works in a few words",
)

print(response.text)
print_token_usage(response)