import openai
import os
import streamlit as st

openai.api_key = os.getenv("OPENAI_API_KEY")

def call_gpt(prompt, langage = 'python', style ='code'):
    """
    This function calls the GPT-3.5-turbo model from OpenAI to generate a response.
    It takes a prompt as input and returns the generated response.
    WIP : optional arguments to change coding langage and output style (pure code, or pegadogic output)
    """
    # Define the messages for the chat completion
    langage_dict = { 
        'python' : 'You are a Python programming assistant.',
        'JS' : 'You are a JavaScript programming assistant.',
        'C' : 'You are a C programming assistant.'
    }
    
    style_dict = { 
        'code' : '''Please respond succinctly. 
         Only code or comments within a single code block in markdown are allowed.
         Do not write text outside the code block.''',
         'pedago' : ''' Please respond with explanations inside the code.
        Help me understand with comments.
        Only code or comments within a single code block in markdown are allowed.
        Do not write text outside the code block.'''
                 }
    messages=[
        {"role": "system", "content": 
        f'''{langage_dict[langage]} {style_dict[style]}
        '''},        
        {"role": "user", "content": prompt}]

    # Call the chat completion API from OpenAI
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=messages,
        temperature=0,
        max_tokens=100,
    )

    # Return the generated response
    return completion['choices'][0]['message']['content']
