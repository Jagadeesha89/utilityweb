import streamlit as st
from hugchat import hugchat
from hugchat.login import Login

email="jaga.m.gowda@gmail.com"
passwd="Jaga@9731"
sign = Login(email, passwd)
cookies = sign.login()
# Save cookies to usercookies/<email>.json
sign.saveCookies()

st.title("ChatGPT-like clone")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
# Response output
## Function for taking user prompt as input followed by producing AI generated responses
def generate_response(prompt):
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    response = chatbot.chat(prompt)
    return response

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in hugchat.ChatBot(cookies=cookies.get_dict()),chatbot.chat(prompt),
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        ):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
