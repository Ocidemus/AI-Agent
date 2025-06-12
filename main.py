import sys
import os 
from dotenv import load_dotenv
from google import genai


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

args = sys.argv
if len(sys.argv) == 1:
    print("Hey Buddy!")
    print("No arguements were given")
    print('Example: python main.py "How do i build a calculator?"')
    sys.exit(1)

response = client.models.generate_content(model='gemini-2.0-flash-001', contents=args[1])

print("Prompt tokens:", response.usage_metadata.prompt_token_count)
print("Response tokens:", response.usage_metadata.candidates_token_count)
print(response.text)

if __name__ == "__main__":
    main()


