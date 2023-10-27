import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def Call_GPT(prompt) : 
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
<<<<<<< HEAD
    messages=[{"role": "user", "content": prompt}
    ],
    # stream = True
=======
    messages=[
        {"role": "system", "content": 
        '''"Tu es un assistant de programmation en python 3, tu réponds de manière succinte'''},
        {"role": "assistant", "content": '''je ne veux que du code ou des commentaires en réponse à l'intérieur d'un bloc de code,
        par exemple si on demande une fonction addition, je veux cette réponse :
        ```def addition(a, b):
        return a + b"}``` '''},        
        {"role": "user", "content": prompt}],
    temperature=0,
    max_tokens=100,
    # stream=True,
>>>>>>> 92ddffe25c9730a230dca831781420dd0c300770
)
    return (completion['choices'][0]['message']['content'])
