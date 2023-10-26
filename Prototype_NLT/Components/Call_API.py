import openai
import os

openai.api_key = os.getenv("OPEN_API_KEY")

def Call_GPT(prompt) : 
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[{"role": "user", "content": prompt}]
)
    return (completion['choices'][0]['message']['content'])