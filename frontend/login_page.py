import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

def login():
    st.title("User Login")
    login_email = st.text_input("Email", key="login_email")
    login_password = st.text_input("Password", type="password", key="login_password")
    if st.button("Login"):
        result = login_user(login_email, login_password)
        if "access_token" in result:
            token = result["access_token"]
            st.session_state.token = token
            st.write("Login successful!")
        else:
            st.write("Login failed!")

def login_user(email, password):
    data = {"email": email, "password": password}
    response = requests.post(f"{BASE_URL}/login", json=data)
    return response.json()
