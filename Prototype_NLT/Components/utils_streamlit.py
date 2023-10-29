from Database.mongodb import insert_in_database, get_database, close_connection
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
    
    # Check if index_session is 0
    if index_session == 0:
        ret = None
        prompt = None
        name = None
    else: 
        # Create a list of sessions from the database
        list_session_db = [y for y in sessions]
        list_session_db.insert(0, 'New_prompt...')
        
        # Get the session based on the index
        dict_session = list_session_db[index_session]
        ret = dict_session['result']
        name = dict_session['username']
        prompt = dict_session['prompt']
    
    # Return the result, username, and prompt
    return ret, name, prompt

def click_prompt():
    st.session_state.prompted = True

def reset_prompt():
    st.session_state.prompted = False