import streamlit as st
import time
import google.generativeai as genai

st.image("/home/sashank/Desktop/gen_ai_bootcamp/03_ui_streamlit/12_chat_app_project/google gemini.webp", width=80)
st.title(" Gemini clone")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    role = message["role"]
    with st.chat_message(role):
        if role == "user":
            st.markdown(message["parts"])
        else:
            st.markdown(message["parts"][0])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "parts": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    placeholder = st.chat_message("model")
    placeholder = placeholder.empty()
    placeholder.markdown("Thinking...")

    # Configure Gemini API
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

    # Initialize the Gemini model
    model = genai.GenerativeModel("gemini-2.5-flash")

    # Start chat session with history
    chat = model.start_chat(history=st.session_state.messages)

    # Send latest user message
    user_input = st.session_state.messages[-1]["parts"]
    response = chat.send_message(user_input)
    full_text = response.text

    # Simulate streaming response (optional)
    with placeholder:
        placeholder = placeholder.empty()
        streamed_text = ""
        for char in full_text:
            streamed_text += char
            placeholder.markdown(streamed_text + "▌")
            time.sleep(0.01)
        placeholder.markdown(streamed_text)

    # Save assistant message
    st.session_state.messages.append({
        "role": "model",
        "parts": [response.text]
    })