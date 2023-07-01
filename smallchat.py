import streamlit as st
from hugchat import hugchat
from hugchat.login import Login
from time import sleep
from hugchat_api import HuggingChat
import os

EMAIL = "jaga.m.gowda@gmail.com"
PASSWD = "Jaga@9731"

HUG= HuggingChat(max_thread=1)

sign=HUG.getSign(EMAIL,PASSWD)
cookies=sign.login(save=True,cookie_dir_path=COOKIE_STORE_PATH)
cookies=sign.loadCookiesFromDir(cookie_dir_path=COOKIE_STORE_PATH)

sign = Login(email, passwd)
cookies = sign.login()

# Save cookies to usercookies/<email>.json
sign.saveCookies()


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
            message_placeholder.markdown(full_response + "▌")
            sleep(0.01)
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
