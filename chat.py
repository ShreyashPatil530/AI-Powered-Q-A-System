import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_question(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]
