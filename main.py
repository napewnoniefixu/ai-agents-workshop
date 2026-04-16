import os
import sys
from dotenv import load_dotenv
from google import genai
from utils import print_token_usage
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
model = "gemini-2.5-flash"

client = genai.Client(api_key=api_key)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py \"your prompt here\"")
        return

    user_input = " ".join(sys.argv[1:])

    response = client.models.generate_content(
        model=model,
        contents=user_input,
    )

    print(response.text)
    print_token_usage(response)

if __name__ == "__main__":
    # main()
    print(write_file(".", "test.txt", "Lorem ipsum"))