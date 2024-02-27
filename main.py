"""This a python file for frontend of the Intelligent Document Finder using LlamaIndex"""
import time
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from rag_query import generate_answer
from extract_metadata import extract_metadata_from_response


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
    add_vertical_space(5)
    add_vertical_space(5)
    st.write('Made with ❤️ by [Sourav Biswas](<https://github.com/souravbiswas19>)')
st.header("🤖Intelligent Document Finder📃🔍")

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"Question: {prompt}")
    response = generate_answer(prompt)
    meta_data = extract_metadata_from_response(response)
    st.write(f"Answer: {response}")
    st.write(f"Source: {meta_data}")