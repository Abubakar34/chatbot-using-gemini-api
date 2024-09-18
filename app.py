from flask import Flask, request, jsonify, redirect, render_template, url_for

import google.generativeai as genai
import groq
from dotenv import load_dotenv
import os
import markdown

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat()

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def handle_message():
    try:
        instruction = """
        Provide a brief answer to the question, and return the response in Markdown format with titles, headings, and lists for better clarity. Use appropriate headers for each section.

        Please provide a detailed yet simple explanation of the following question. Ensure the explanation is easy to understand for someone unfamiliar with the topic. Include a real-world example to illustrate the concept clearly: \n"""
        data = request.get_json()
        prompt = data.get("message", "")

        response = chat.send_message(instruction + prompt)
        html_response = markdown.markdown(response.text)

        return jsonify({"response": html_response})

    except Exception as e:
        # return jsonify({"prompt": prompt})
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
