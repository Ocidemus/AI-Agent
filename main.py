import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

from prompts import system_prompt
from call_function import available_functions
from call_function import call_function


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    verbose = "--verbose" in sys.argv
    client = genai.Client(api_key=api_key)

    args = sys.argv[1:]
    if len(sys.argv) == 1:
        print("Hey Buddy!")
        print("No arguements were given")
        print('Example: python main.py "How do i build a calculator?"')
        sys.exit(1)

    user_prompt = " ".join(args)
    if verbose:
        print(f"User prompt: {user_prompt}\n")
    messages = [
            types.Content(role="user", parts = [types.Part(text=user_prompt)]),           
        ]

    generate_content(client,messages,verbose)
    
        
    
def generate_content(client,messages,verbose):
    for _ in range(20):
        response = client.models.generate_content(
            model='gemini-2.0-flash-001',
            contents=messages,
            config=types.GenerateContentConfig(tools=[available_functions],system_instruction=system_prompt) )
            
        if verbose:
            
            print("Prompt tokens:", response.usage_metadata.prompt_token_count)
            print("Response tokens:", response.usage_metadata.candidates_token_count)
        
        if not response.function_calls:
            return response.text

        for candidate in response.candidates[:20]:
            messages.append(candidate.content)
        
        function_responses = []
        if response.function_calls:
            for function_call_part in response.function_calls:
                function_call_result = call_function(function_call_part, verbose)

                if (
                    not function_call_result.parts
                    or not function_call_result.parts[0].function_response
                ):
                    raise Exception("empty function call result")

                if verbose:
                    print(f"-> {function_call_result.parts[0].function_response.response}")

                function_responses.append(function_call_result.parts[0])

            if not function_responses:
                raise Exception("no function responses generated, exiting.")

            for func_response_part in function_responses:
                messages.append(types.Content(role="function", parts=[func_response_part]))

            continue  # function was called, so loop again

    
        print(response.text)
        break
        

        
if __name__ == "__main__":
    main()


