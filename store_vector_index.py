import os
from config import config
from google_drive_reader import docs
from gemini_llm import llm, embed_model
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.core import Settings

Settings.llm = llm
Settings.embed_model = embed_model
PERSIST_DIR = config['PERSIST_DIR']

if not os.path.exists(PERSIST_DIR):
    #load the document and create the index
    index = VectorStoreIndex.from_documents(docs, embed_model=embed_model)
    #store for it for later
    index.storage_context.persist(persist_dir=PERSIST_DIR)
else:
    #load the existing index
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)