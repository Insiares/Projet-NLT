import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()

# Example OpenAI Python library request
MODEL = "gpt-3.5-turbo"
response = openai.ChatCompletion.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "Tu es un enseignant python? Des élèves vont te demander comment coder des fonctionnalités. "},
        {"role": "user", "content": "Knock knock."},
        {"role": "assistant", "content": "Who's there?"},
        {"role": "user", "content": "Orange."},
    ],
    temperature=0,
)

print(response)