import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai import *
from prompts import system_prompt
from functions.get_files_info import *



def main():
    load_dotenv()
    
    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    model_name = 'gemini-2.0-flash-001'

    user_prompt = " ".join(args)

    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),]

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
        ]
    )
   
    def generate_content(client, messages, verbose):

        response = client.models.generate_content(
            model=model_name,
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions],
                system_instruction=system_prompt,
            ),
        )

        if verbose:
            print(f"User prompt: {user_prompt}")
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

        print("Response:")
        print(response.text)
        if response.function_calls:
            for function_call_part in response.function_calls:
                print(f"Calling function: {function_call_part.name}({function_call_part.args})")

    generate_content(client=client, messages=messages, verbose=verbose)
    

if __name__ == "__main__":
    main()
