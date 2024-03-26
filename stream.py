import streamlit as st
import requests

# Define the base URL for your FastAPI server
BASE_URL = "http://127.0.0.1:8000"
# BASE_URL = "http://127.0.0.1:8000/"
# Function to register a new user
def register_user(username, email, password):
    data = {"username": username, "email": email, "password": password}
    response = requests.post(f"{BASE_URL}/register", json=data)
    return response.json()

# Function to log in a user
def login(email, password):
    data = {"email": email, "password": password}
    response = requests.post(f"{BASE_URL}/login", json=data)
    return response.json()

# Function to query for an answer
def query(question, token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BASE_URL}/getquery", data=question, headers=headers)
    return response.json()

# Streamlit app
def main():
    st.title("FastAPI with Streamlit Frontend")

    # User registration
    st.header("User Registration")
    reg_username = st.text_input("Username", key="reg_username")
    reg_email = st.text_input("Email", key="reg_email")
    reg_password = st.text_input("Password", type="password", key="reg_password")
    if st.button("Register"):
        result = register_user(reg_username, reg_email, reg_password)
        st.write(result)

    # User login
    st.header("User Login")
    login_email = st.text_input("Email", key="login_email")
    login_password = st.text_input("Password", type="password", key="login_password")
    if st.button("Login"):
        result = login(login_email, login_password)
        if "access_token" in result:
            token = result["access_token"]
            st.write("Login successful!")
        else:
            st.write("Login failed!")

    # Query for an answer
    st.header("Query")
    if "token" in locals():
        question = st.text_input("Enter your question", key="question")
        if st.button("Ask"):
            result = query(question, token)
            if "answer" in result:
                st.write("Answer:", result["answer"])
            else:
                st.write("Failed to get an answer.")

if __name__ == "__main__":
    main()
