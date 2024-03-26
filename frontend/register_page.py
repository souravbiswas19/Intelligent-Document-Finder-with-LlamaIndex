import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

def register():
    st.title("User Registration")
    reg_username = st.text_input("Username", key="reg_username")
    reg_email = st.text_input("Email", key="reg_email")
    reg_password = st.text_input("Password", type="password", key="reg_password")
    if st.button("Register"):
        result = register_user(reg_username, reg_email, reg_password)
        st.write(result)

def register_user(username, email, password):
    data = {"username": username, "email": email, "password": password}
    response = requests.post(f"{BASE_URL}/register", json=data)
    return response.json()
