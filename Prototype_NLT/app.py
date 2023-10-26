from Components.Call_API import Call_GPT
import streamlit as st

st.title("Prototype Chat_GPT")

Prompt = st.text_area(label= 'prompt',label_visibility='hidden',placeholder=f"Décris-moi la fonction Python souhaitée :")

if Prompt:
    st.write('prompt:',str(Prompt))

if st.button(label="Generate,"):
    ret = Call_GPT(Prompt)
    st.write(ret)