from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv() 

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("OPENAI_API_KEY environment variable is missing!")

client = OpenAI(api_key=api_key)

def chat_with_openai(messages):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        print("OpenAI API call failed:", e)
        return "Sorry, I couldn't process your request."