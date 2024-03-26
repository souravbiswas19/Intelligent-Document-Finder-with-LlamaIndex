import streamlit as st
from register_page import register
from login_page import login
from query_page import query

# Page titles and functions mapping
PAGES = {
    "Register": register,
    "Login": login,
    "Query": query,
}

def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    if selection == "Query":
        if "token" not in st.session_state:
            st.sidebar.warning("Please login first.")
            return
    # Display the selected page content
    page = PAGES[selection]
    page()

if __name__ == "__main__":
    main()
