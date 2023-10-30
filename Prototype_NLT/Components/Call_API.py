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
    langage_dict = { 'python' : 'You are a Python senior programmer.',
                      'JS' : 'You are a JavaScript senior programmer.',
                      'C' : 'You are a C senior programmer.'}
    style_dict = { 'code' : '''Respond only with non-formatted code. 
                  Do not write text outside the code block.
                  No example usage.
                  No output example.
                  if something absolutely needs clarification, do so as a comment inside the code.''',
                    'pedago' : ''' Please respond with explanations inside the code.
                                Help me understand with comments.
                    Only code or comments within a single code block in markdown are allowed.
         Do not write text outside the code block.'''}
    
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
