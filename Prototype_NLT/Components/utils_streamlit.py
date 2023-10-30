from Database.mongodb import get_database 
import streamlit as st

def variable_session(index_session, name):
    """
    This function retrieves session data from a database based on the provided index and name.
    
    :param index_session: Index of the session to retrieve.
    :param name: Name of the database.
    :return: A tuple containing the result, username, and prompt from the session.
    """
    # Get the database and client
    sessions, client = get_database(name)
    

    # Create a list of sessions from the database
    list_session_db = [y for y in sessions]
    # list_session_db.insert(0, '0')
    
    # Get the session based on the index
    dict_session = list_session_db[index_session]
    ret = dict_session['result']
    name = dict_session['username']
    prompt = dict_session['prompt']
    
    # Return the result, username, and prompt
    return ret, name, prompt

# switch function for enabling and disabling buttons
def run_disable():
    st.session_state.running = True

def enable():
    st.session_state.running = False
