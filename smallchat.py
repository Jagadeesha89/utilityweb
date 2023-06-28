import streamlit as st
from hugchat import hugchat
from hugchat.login import Login

email = "jaga.m.gowda@gmail.com"
passwd = "Jaga@9731"
sign = Login(email, passwd)
cookies = sign.login()

st.title("ChatGPT-like clone")

messages = []

def append_message(role, content):
    global messages
    messages.append({"role": role, "content": content})


def get_response(prompt):
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    for message in messages:
        chatbot.append_message(role=message["role"], content=message["content"])

    full_response = ""
    for response in chatbot.chat(stream=False):
        full_response += response.choices[0].delta.get("content", "")
    return full_response

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("What is up?")
if prompt:
    append_message("user", prompt)
    full_response = get_response(prompt)
    append_message("assistant", full_response)
    with st.chat_message("assistant"):
        st.markdown(full_response)
