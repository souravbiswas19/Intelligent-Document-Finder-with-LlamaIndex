"""This module is responsible for initializing LLM, Embedding and Prompts"""
# Necessary libraries are being imported
import os
from config import config
from llama_index.llms.gemini import Gemini
from llama_index.core.prompts.prompts import SimpleInputPrompt
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
try:
    #loading the GOOGLE_API_KEY variable in the environment
    os.environ["GOOGLE_API_KEY"] = config['GOOGLE_API_KEY']

    #Designing the System Prompt and Query Wrapper Prompt
    system_prompt = """
    You are a Q&A assistant. Your goal is to answer questions as
    accurately as posssible based on the instruction and context provided.
    We have provided context information below.
    Given this information, please answer the question:
    """
    query_wrapper_prompt = SimpleInputPrompt("<|USER|>{query_str}<|ASSISTANT|>")
    #Gemini is being initialized as llm
    llm = Gemini()
    #System Prompt is being initialized to the llm
    llm.system_prompt = system_prompt
    #Query Wrapper Prompt is being initialized to the llm
    llm.query_wrapper_prompt = query_wrapper_prompt
    #embedding model is being initialized from Huggingface
    embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
except Exception as e: # When error is encountered while loading the llm and embedding model
    print("Error while loading model")