import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

def query():
    st.title("Query")
    question = st.text_input("Enter your question", key="question")
    if st.button("Ask"):
        result = query_answer(question)
        if result:
            st.write("Answer:", result["answer"]["response"])
            metadata = result["answer"]["source_nodes"][0]["node"]["metadata"]
            st.write("Source:", metadata)
        else:
            st.write("Failed to get an answer.")

def query_answer(question):
    token = st.session_state.get("token")
    if token:
        print(token)
        headers = {"Authorization": f"Bearer {token}"}
        # oneresp = requests.get(f"{BASE_URL}/getGoogleDriveData", headers=headers)
        # gresp = requests.get(f"{BASE_URL}/getOnedriveData", headers=headers)
        response = requests.post(f"{BASE_URL}/getquery", json={"question": question}, headers=headers)
        return response.json()
    else:
        st.write("Please login first.")
