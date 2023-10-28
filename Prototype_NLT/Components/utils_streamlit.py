from Database.mongodb import insert_in_database, get_database, close_connection
import streamlit as st

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

def reset_prompt():
    st.session_state.prompted = False