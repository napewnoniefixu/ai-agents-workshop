import os
import sys
from dotenv import load_dotenv
from google import genai
from utils import print_token_usage
from google.genai import types
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from tools import tools

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
model = "gemini-2.5-flash"

client = genai.Client(api_key=api_key)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py \"your prompt here\"")
        return

    user_input = " ".join(sys.argv[1:])

    messages = [
        types.Content(
            role="user",
            parts=[
                types.Part(text=user_input)
            ]
        )
    ]

    response = client.models.generate_content(
    model=model,
    contents=messages,
    config=types.GenerateContentConfig(
        tools=tools,
        system_instruction="You are a coding agent. Use tools to solve tasks."
    ),
    )

    if response.function_calls:
        for function_call in response.function_calls:
            print(f"Calling function {function_call.name}")
    else:
        print(response.text)
        print_token_usage(response)

if __name__ == "__main__":
    main()
    # print(write_file(".", "test.txt", "Lorem ipsum"))