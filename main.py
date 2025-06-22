import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

from prompts import system_prompt
from call_function import available_functions


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    args = sys.argv[1:]
    if len(sys.argv) == 1:
        print("Hey Buddy!")
        print("No arguements were given")
        print('Example: python main.py "How do i build a calculator?"')
        sys.exit(1)

    user_prompt = " ".join(args)
    
    messages = [
            types.Content(role="user", parts = [types.Part(text=user_prompt)]),           
        ]

    generate_content(client,messages,user_prompt)
    
        
    
def generate_content(client,messages,inputed):
    response = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages,config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt) )
         
    if "--verbose" in inputed:
        print("User prompt:", inputed)
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    
    if not response.function_calls:
        return response.text

    for function_call_part in response.function_calls:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")

if __name__ == "__main__":
    main()


