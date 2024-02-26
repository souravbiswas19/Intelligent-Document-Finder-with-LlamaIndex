import os
from llama_index.llms.gemini import Gemini
from llama_index.core.prompts.prompts import SimpleInputPrompt
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from config import config
os.environ["GOOGLE_API_KEY"] = config['GOOGLE_API_KEY']
system_prompt = """
You are a Q&A assistant. Your goal is to answer questions as
accurately as posssible based on the instruction and context provided
"""
## Default format supported by Llama2
query_wrapper_prompt = SimpleInputPrompt("<|USER|>{query_str}<|ASSISTANT|>")
llm = Gemini()
llm.system_prompt = system_prompt
llm.query_wrapper_prompt = query_wrapper_prompt #prompt
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")