import google.generativeai as genai
import groq
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")

chat = model.start_chat()
prompt = "What is Ai?"
instruction = "Provide the brief answer of the question and provide real world examples for clarity and ture understanding of the concept: \n"

response = chat.send_message(instruction + prompt)
print(f"The response is:\n {response.text}")
