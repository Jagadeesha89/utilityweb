import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from hugchat import hugchat
from hugchat.login import Login


email="jaga.m.gowda@gmail.com"
passwd="Jaga@9731"
sign = Login(email, passwd)
cookies = sign.login()

# Save cookies to usercookies/<email>.json
sign.saveCookies()
# Response output
## Function for taking user prompt as input followed by producing AI generated responses
def generate_response(prompt):
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    response = chatbot.chat(prompt)
    return response
# Set the layout of the app
st.layout = st.container()

# Add a text input field
text_input = st.text_input("Enter your message")

# If the user enters a message, generate the result and display it
if text_input:
  # Get the user's query
  query = text_input

  # Generate the result
  result = generate_response(query)

  # Display the user's query, the result, and the conversation history
  st.write("User query:", query)
  st.write("Result:", result)
  st.write("Conversation history:")
  for message in chat._conversation_history:
    st.write(message)

  # Once the user clicks on enter, remove the query from the prompt box
  st.text_input("Enter your message", key=None)

  # Display the generated response in typewriter effect
  st.write(result, unsafe_allow_html=True, key="generated_response")
  st.markdown("""
  <style>
  #generated_response {
  animation: typewriting 2s infinite;
  }

  @keyframes typewriting {
    0% {
      opacity: 0;
    }
    25% {
      opacity: 1;
    }
    100% {
      opacity: 0;
    }
  }
  </style>
  """, unsafe_allow_html=True)
