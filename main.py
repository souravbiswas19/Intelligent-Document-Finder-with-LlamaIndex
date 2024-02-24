import streamlit as st
import time
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space

with st.sidebar:
    body = "🤖Intelligent Document Finder📃🔍"
    st.header(body)
    st.markdown('''
    ## About
    This app is an LLM-powered Intelligent Document Finder:
    - [LlamaIndex](<https://www.llamaindex.ai/>)
    - [GoogleGemini](<https://gemini.google.com/>)
    - [HuggingFace](<https://huggingface.co/>) LLM model
    
    ''')
    # st.button("Reload from Google Drive", type="primary")
    # if st.button('Say hello'):
    #     st.write('Why hello there')
    # else:
    #     st.write('Goodbye')
    add_vertical_space(5)
    add_vertical_space(5)
    st.write('Made with ❤️ by [Sourav Biswas](<https://github.com/souravbiswas19>)')
st.header("🤖Intelligent Document Finder📃🔍")
# st.header("Your Query Here👇🏽")
# title = st.text_input('')
# print(title)
prompt = st.chat_input("Say something")
if prompt:
    """
    Reload the google drive after every prompt
    1. Will increase the processing time
    2. Will check if there is any new documents that has been uploaded in the folder
    """

    """
    Query to be passed to the function to fetch the answer to the query
    """

    st.write(f"User has sent the following prompt: {prompt}")

