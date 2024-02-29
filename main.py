"""This a python file for frontend of the Intelligent Document Finder using LlamaIndex"""
#Necessary files are being fetched
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from rag_query import generate_answer
from extract_metadata import extract_metadata_from_response

# Sidebar for the description of the project
with st.sidebar:
    # Designing the Sidebar to describe the project
    body = "🤖Intelligent Document Finder📃🔍"
    st.header(body)
    st.markdown('''
    ## About
    This app is an LLM-powered Intelligent Document Finder developed using:
    - [LlamaIndex](<https://www.llamaindex.ai/>)
    - [GoogleGemini](<https://gemini.google.com/>)
    - [HuggingFace](<https://huggingface.co/>) LLM model
    
    ''')
    add_vertical_space(5)
    add_vertical_space(5)
    st.write('Made with ❤️ by [Sourav Biswas](<https://github.com/souravbiswas19>)')
st.header("🤖Intelligent Document Finder📃🔍")

try:
    # Front end part for the passing of the prompt and generating the answer and metadata
    prompt = st.chat_input("Say something")
    if prompt:
        # Template for the Question section
        st.header("Question:")
        # Displaying the prompt question
        st.write(prompt)
        # Generatin the answer from the prompt
        response = generate_answer(prompt)
        # Extracting the metadata from the response/answer
        meta_data = extract_metadata_from_response(response)
        # Displaying the answer
        st.header("Answer:")
        # Displaying the response returned by the query engine
        st.write(response.response)
        # Displaying the Metadata
        st.header("Source:")
        # Displaying the metadata - document_title - Title
        st.write(f"Document Title: {meta_data['document_title']}")
        # Displaying the metadata - file_name - File Name
        st.write(f"File Name: {meta_data['file name']}")
        # Displaying the metadata - page_lable -> Page Number
        st.write(f"Page Number: {meta_data['page_label']}")
except RuntimeError as e:
    st.write(f"Error occurred: {e}")
# End of File