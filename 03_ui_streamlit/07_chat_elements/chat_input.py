# https://docs.streamlit.io/library/api-reference/chat/st.chat_input

import streamlit as st

prompt = st.chat_input("Say something to be added to data")


if 'data' not in st.session_state:
    st.session_state.data  = []

if prompt:
    st.session_state.data.append(prompt)
    for text in st.session_state.data:
        st.write(f"User has sent the following prompt: {text}") #shows all text sent in so far as text

st.write(st.session_state.data) #shows all text sent in so far as a list

