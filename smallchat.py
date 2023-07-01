import streamlit as st
from hugchat import hugchat
from hugchat.login import Login
from time import sleep
from hugchat_api import HuggingChat
import os

EMAIL = st.secrets["DB_EMAIL"]
PASSWD = st.secrets["DB_PASS"]
COOKIE_STORE_PATH = "./usercookies"

HUG= HuggingChat(max_thread=1)

sign=HUG.getSign(EMAIL,PASSWD)
cookies=sign.login(save=True,cookie_dir_path=COOKIE_STORE_PATH)
cookies=sign.loadCookiesFromDir(cookie_dir_path=COOKIE_STORE_PATH)


st.title("ChatGPT-like clone")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        def generate_response(prompt):
            chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
            response = chatbot.chat(prompt, stream=True)
            if isinstance(response, str):
                return response
            else:
                return response.delta.get("content", "")

        for response in generate_response(prompt):
            full_response += response
            with st.spinner("Generating Report....\nplease wait...."):
                 message_placeholder.markdown(full_response + "▌")
                 sleep(0.01)
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
