import streamlit as st 
from Components.Call_API import call_gpt
from Components.utils_streamlit import variable_session, run_disable, enable
from time import time
from Database.mongodb import insert_in_database, get_database, close_connection, update_database
import sys
from io import StringIO

# ----------------------- session state declaration -----------------------
if 'prompt' not in st.session_state:
    st.session_state.prompt = ' '

if 'running' not in st.session_state:
    st.session_state.running = False

if 'result' not in st.session_state:
    st.session_state.result = ' '

if 'name' not in st.session_state:
    st.session_state.name = 'anon'

# ------------------------- App Layout ------------------------------------
#title
st.title('NLT By LesNuls')

#Sidebar
with st.sidebar: 
    sessions, client = get_database(st.session_state.name)
    list_session_prompt = [str(y['prompt'][:25]+'...') for y in sessions]
    
    st.subheader('Sessions')

    if st.button('Reset'):
        st.session_state.result = ' '
        st.session_state.prompt = ' '
        
    st.text_input(label= 'Your Name',
                    # label_visibility='hidden',
                         placeholder=f"Enter your name", 
                         value='Anonyme',
                         key='name')
   
    option = st.radio(label='Select Past Prompt',options=[y for y in list_session_prompt])

    selected_index = list_session_prompt.index(option)
    ret_, nom, prompt_ = variable_session((selected_index), st.session_state.name)
    st.session_state.result =ret_
    st.session_state.prompt = prompt_

#Input Area for prompt
st.text_area(
             label_visibility='visible',
             value=st.session_state.prompt,
             key='prompt',
             on_change=enable,
             label= '''Enter your demand in this area, 
             if you modify it and want to ask again, 
             don't forget to validate by hitting CTRL+Enter''',)

if st.button(label='Generate', on_click=run_disable, disabled=st.session_state.running):
    with st.spinner('Working AI magic...'):
        st.session_state.result = call_gpt(st.session_state.prompt)
        st.success('Done!', icon='✅')
        insert_in_database(st.session_state.prompt, st.session_state.result, st.session_state.name)
        sessions, client = get_database(st.session_state.name)
        close_connection(client)

st.text_area(label='Result area', label_visibility='hidden', value=st.session_state.result)

close_connection(client)