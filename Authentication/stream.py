import json
import streamlit as st
import requests
# Create an empty container
placeholder = st.empty()

# Insert a form in the container
with st.sidebar:
    options = st.selectbox('Login/Register',('Register', 'Login'))
    if options == 'Register':
        with placeholder.form("Signup"):
            st.markdown("#### SignUP")
            name = st.text_input("Name")
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            submit = st.form_submit_button("Signup")

        user_signup_details = {
        "username": name,
        "email": email,
        "password": password
        }
        user_login_details = {
        "email": email,
        "password": password
        }

        if submit:
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
            submit = st.form_submit_button("Signup")

        user_login_details = {
        "email": email,
        "password": password
        }

        if submit:
            placeholder = st.empty()
            res = requests.post(url="http://127.0.0.1:8000/login", data=json.dumps(user_login_details))
            if res.status_code == 200:
                st.write(res.content)
                st.success("Login successful")
            else:
                st.write(res.content)
                st.error("Login Failed")