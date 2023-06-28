import streamlit as st
from hugchat import hugchat
from hugchat.login import Login

email = "jaga.m.gowda@gmail.com"
passwd = "Jaga@9731"
sign = Login(email, passwd)
cookies = sign.login()

st.title("ChatGPT-like clone")

messages = []

def get_response(prompt):
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    full_response = ""
    for response in chatbot.chat(text=prompt, stream=False):
        full_response += response.choices[0].delta.get("content", "")
    return full_response

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("What is up?")
if prompt:
    messages.append({"role": "user", "content": prompt})
    full_response = get_response(prompt)
    messages.append({"role": "assistant", "content": full_response})
    with st.chat_message("assistant"):
        st.markdown(full_response)
