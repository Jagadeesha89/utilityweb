import streamlit as st
from hugchat import hugchat
from hugchat.login import Login

email = "jaga.m.gowda@gmail.com"
passwd = "Jaga@9731"
sign = Login(email, passwd)
cookies = sign.login()
# Save cookies to usercookies/<email>.json
sign.saveCookies()

st.title("ChatGPT-like clone")

messages = []

def get_response(prompt):
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    full_response = ""
    response = chatbot.chat(prompt, stream=True)
    if isinstance(response, str):
        full_response += response
    else:
        for choice in response.choices:
            full_response += choice.delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    return full_response

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("What is up?")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    full_response = get_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    with st.chat_message("assistant"):
        st.markdown(full_response)
