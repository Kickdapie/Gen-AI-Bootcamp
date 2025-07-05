# https://docs.streamlit.io/library/api-reference/layout/st.sidebar

import streamlit as st

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
) 


# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
<<<<<<< HEAD


#TODO: add a callback function
def onChange(method):
    text = ''
    if method == "Email":
        text = st.text_input("Provide your email.")
    elif method == "Home phone":
        text = st.text_input("Provide your number.")
    else:
        text = st.text_input("Provide your number.")
    st.write(f"You entered {text}")

onChange(add_selectbox)
=======
>>>>>>> sashank/main
