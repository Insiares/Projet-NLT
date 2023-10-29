import openai
import os
import streamlit as st

openai.api_key = os.getenv("OPENAI_API_KEY")

def call_gpt(prompt):
    """
    This function calls the GPT-3.5-turbo model from OpenAI to generate a response.
    It takes a prompt as input and returns the generated response.
    """
    # Define the messages for the chat completion
    messages = [
        {"role": "system", 
         "content": '''You are a Python programming assistant. 
         Please respond succinctly. 
         Only code unformatted allowed.
         Do not write text outside the code block.
         '''},
        {"role": "user", "content": "give me a function for addition"},
        {"role": "assistant", "content": "```def addition(a, b):\n return a + b```"},        
        {"role": "user", "content": prompt}
    ]

    # Call the chat completion API from OpenAI
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=messages,
        temperature=0,
        max_tokens=100,
    )

    # Return the generated response
    return completion['choices'][0]['message']['content']
