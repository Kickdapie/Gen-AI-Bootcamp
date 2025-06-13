# https://docs.streamlit.io/library/api-reference/chat/st.chat_message

import streamlit as st
import numpy as np

message = st.chat_message("assistant") #This is the chat talking and giving data to user
message.write("Hello human")
message.bar_chart(np.random.randn(30, 3))

message1 = st.chat_message("user") #This is the user talking
message1.write("Thanks")
