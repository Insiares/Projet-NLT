from Components.Call_API import Call_GPT
import streamlit as st

st.title("Prototype Chat_GPT")

Prompt = st.text_area(label= 'prompt',label_visibility='hidden',placeholder=f"Décris-moi la fonction Python souhaitée :")

if 'prompted' not in st.session_state:
    st.session_state.prompted = False

def click_prompt():
    st.session_state.prompted = True

cols_up1, cols_up2 = st.columns([3,1])

def reset_prompt():
    st.session_state.prompted = False

#Caching API Call
@st.cache_data
def Call(Input):
    output = Call_GPT(Input)
    return output

with cols_up2:
    bip = st.button(label="Generate", on_click=click_prompt, disabled=st.session_state.prompted)

#splitting bottom of page
cols_bot1, cols_bot2 = st.columns(2)



if bip:
    ret = Call(Prompt)
    with cols_bot1:
        Output = st.text_area(label='AI Output', value=ret)
    with cols_bot2:
        st.markdown(Output)
    with cols_up2:
        st.button(label='Prompt Again', on_click=reset_prompt, disabled=not st.session_state.prompted)

        
#Declaring a sidebar with session History

with st.sidebar:
    st.subheader('Sessions')
    st.button('Debug', on_click=reset_prompt)

