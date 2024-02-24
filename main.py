import streamlit as st
import time
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space

with st.sidebar:
    body = "🤖Intelligent Document Finder📃🔍"
    st.header(body)
    add_vertical_space(5)
    st.markdown('''
    ## About
    This app is an LLM-powered Intelligent Document Finder:
    - [LlamaIndex](<https://www.llamaindex.ai/>)
    - [GoogleGemini](<https://gemini.google.com/>)
    - [HuggingFace](<https://huggingface.co/>) LLM model
    
    ''')
    add_vertical_space(5)
    st.write('Made with ❤️ by [Sourav Biswas](<https://github.com/souravbiswas19>)')

st.header("Your Query Here👇🏽")
title = st.text_input()
print(title)
latest_iteration = st.empty()
bar = st.progress(0)

if title:
  for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Searching for your query... {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

  '...and now we\'re done!✅'
  st.write('Answer is: ', title)
# 'Starting a long computation...'

# Add a placeholder
