import os
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from config import config
os.environ["GOOGLE_API_KEY"] = config['GOOGLE_API_KEY']
"""
Define Prompts here
"""
llm = Gemini()
llm.system_prompt = "" #prompt
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
print(llm)
print(embed_model)