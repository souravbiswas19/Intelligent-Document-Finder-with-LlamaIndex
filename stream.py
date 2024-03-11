import json
import os
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
import requests


def idf():
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
            response = requests.post(url="http://127.0.0.1:8000/getquery", data=json.dumps(prompt))
            # Extracting the metadata from the response/answer
            # meta_data = extract_metadata_from_response(response)
            # # Displaying the answer
            st.header("Answer:")
            # # Displaying the response returned by the query engine
            st.write(response.response)
            # # Displaying the Metadata
            # st.header("Source:")
            # # Displaying the metadata - document_title - Title
            # st.write(f"Document Title: {meta_data['document_title']}")
            # # Displaying the metadata - file_name - File Name
            # st.write(f"File Name: {meta_data['file name']}")
            # # Displaying the metadata - page_lable -> Page Number
            # st.write(f"Page Number: {meta_data['page_label']}")
    except RuntimeError as e:
        st.write(f"Error occurred: {e}")

# Create an empty container
placeholder = st.empty()
# Insert a form in the container
options = st.selectbox('Login/Register',('Register', 'Login'))
if options == 'Register':
    with placeholder.form("Signup"):
        st.markdown("#### SignUP")
        name = st.text_input("Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        signup_button = st.form_submit_button("Signup")
    user_signup_details = {
    "username": name,
    "email": email,
    "password": password
    }
    # user_login_details = {
    # "email": email,
    # "password": password
    # }
    if signup_button:
        placeholder = st.empty()
        res = requests.post(url="http://127.0.0.1:8000/register", data=json.dumps(user_signup_details))
        if res.status_code == 200:
            st.write(res.content)
            st.success("SignUp successful")
        else:
            st.write(res.content)
            st.error("SignUp Failed")
if options == 'Login':
    with placeholder.form("login"):
        st.markdown("#### Login")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        login_button = st.form_submit_button("Login")

    user_login_details = {
    "email": email,
    "password": password
    }

    if login_button:
        placeholder = st.empty()
        res = requests.post(url="http://127.0.0.1:8000/login", data=json.dumps(user_login_details))
        token_dict = json.loads(res.content)
        if res.status_code == 200:
            # st.write(token_dict['access_token'])
            st.success("Login successful")
            access_token = token_dict['access_token']
            if access_token:
                st.query_params["access_token"]=access_token
                st.header("Google Drive Link")
                link = st.text_input("Link")
                fetch_button = st.button("Fetch")
                resp = requests.post(
                    "http://127.0.0.1:8000/setlink", 
                    data=json.dumps({"link": link}), 
                    headers={"accept": "application/json","Authorization": f"Bearer {access_token}", "Content-Type": "application/json" })
                if resp:
                    st.write("Fetched Successfully")
            else:
                st.error("Login failed. Incorrect username or password.")
        else:
            st.write(res.content)
            st.error("Login Failed")