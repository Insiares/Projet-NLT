from Components.Call_API import Call_GPT
import streamlit as st
from time import time, sleep
from Database.mongodb import insert_in_database, get_database, close_connection

st.title("Prototype Chat_GPT")

name = st.text_input(label= 'Nom',label_visibility='hidden',placeholder=f"Entrez votre nom")
Prompt = st.text_area(label= 'prompt',label_visibility='hidden',placeholder=f"Décris-moi la fonction Python souhaitée :")

if 'prompted' not in st.session_state:
    st.session_state.prompted = False

def variable_session(index_session, name):
    sessions, client = get_database(name)
    if index_session == 0:
        ret= None
        prompt = None
        name = None

    else: 
        list_session_db= [y for y in sessions]
        list_session_db.insert(0, 'New_prompt...')
        dict_session = list_session_db[index_session]
        ret = dict_session['result']
        name = dict_session['username']
        prompt = dict_session['prompt']
    return ret, name, prompt

def click_prompt():
    st.session_state.prompted = True

cols_up1, cols_up2 = st.columns([3,1])

def reset_prompt():
    st.session_state.prompted = False

with st.sidebar:
    st.subheader('Sessions')
    st.button('Debug', on_click=reset_prompt)

#Caching API Call
@st.cache_data
def Call(Input):
    output = Call_GPT(Input)
    return output

with cols_up2:
    bip = st.button(label="Generate", on_click=click_prompt, disabled=st.session_state.prompted)

#splitting bottom of page
cols_bot1, cols_bot2 = st.columns(2)

ret = None

if bip:
    heure = time()
    ret = Call(Prompt)
    duree = round((time() - heure), 2)
    st.write(f" Le résultat a mis {duree} secondes à être généré")


if ret is not None:
    insert_in_database(Prompt, ret, name)
    sessions, client = get_database(name)
    close_connection(client)

#Declaring a sidebar with session History
with st.sidebar: 
    sessions, client = get_database(name)
    list_session_prompt = [str(y['prompt'][:25]+'...') for y in sessions]
    list_session_prompt.insert(0, 'New_prompt...')
    selected_option = st.radio('Select Past Prompt', [y for y in list_session_prompt])
    if selected_option != 'New_prompt...':
        selected_index = list_session_prompt.index(selected_option)
        ret_, nom, prompt = variable_session(selected_index, name)
        ret=ret_

sessions, client = get_database(name)
for session in sessions:
    st.write(session)

with cols_bot1:
    Output = st.text_area(label='AI Output', value=ret, key=1)
with cols_bot2:
    st.markdown(Output)
with cols_up2:
    st.button(label='Prompt Again', on_click=reset_prompt, disabled=not st.session_state.prompted)
    
close_connection(client)