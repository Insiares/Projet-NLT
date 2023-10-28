import openai
import os

openai.api_key = os.getenv("OPEN_API_KEY")

def Call_GPT(prompt) : 
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=[
        {"role": "system", "content": 
        '''"Tu es un assistant de programmation en python 3, tu réponds de manière succinte. 
        je ne veux en retour que du code ou des commentaires, à l'intérieur d'un unique bloc de code en markdown.
        Il est interdit d'écrire du texte en dehors du bloc de code.'''},
        {"role": "user", "content": '''donne moi une fonction d'addition'''},
        {"role": "assistant", "content":" ```def addition(a, b): \n return a + b``` "},        
        {"role": "user", "content": prompt}],
    temperature=0,
    max_tokens=100,
    # stream=True,
)
    return (completion['choices'][0]['message']['content'])
