# https://docs.streamlit.io/library/api-reference/layout/st.empty

# Inserts a container into your app that can be used to hold a single element. 

import streamlit as st
import time

st.title("Danny")



with st.empty():
    for seconds in range(10):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
    st.write("✔️ 10 seconds over!")

<<<<<<< HEAD
st.write("Danny was here") #text appears after 10 seconds have passed
=======
st.write("Pakistan zinda bad")
>>>>>>> sashank/main
