from Components.Call_API import Call_GPT
import streamlit as st
from time import time, sleep
from Database.mongodb import insert_in_database, get_database, close_connection

st.title("Prototype Chat_GPT")

name = st.text_input(label= 'Nom',label_visibility='hidden',placeholder=f"Entrez votre nom")
Prompt = st.text_area(label= 'prompt',label_visibility='hidden',placeholder=f"Décris-moi la fonction Python souhaitée :")

if Prompt:
    st.write('prompt:',str(Prompt))

if st.button(label="Generate"):
    heure = time()
    ret = Call_GPT(Prompt)
    st.write(ret)
    duree = round((time() - heure), 2)
    st.write(f" Le résultat a mis {duree} secondes à être généré")
    insert_in_database(Prompt, ret, name)
    sessions, client = get_database(name)
    for session in sessions:
        st.markdown(f"Username: {session['username']}<br>Prompt: {session['prompt']}<br>Result: {session['result']}", unsafe_allow_html=True)
    close_connection(client)