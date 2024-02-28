"""
This python module performs the function of storing 
the vectors along with the implementation of TitleExtractor
"""
#importing the necessary libraries
import os
from google_drive_reader import docs
from gemini_llm import llm, embed_model
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage, Settings
from llama_index.core.extractors import TitleExtractor
from llama_index.core.node_parser import TokenTextSplitter
from llama_index.core.ingestion import IngestionPipeline

def store_index():
    #Initializing the LLM model, embedding model and chunk size
    Settings.llm = llm
    Settings.embed_model = embed_model
    Settings.chunk_size = 1024
    #Initializing the PERSISTENT DIRECTORY path
    PERSIST_DIR = "./storage"

    #Initializing TokenTextSplitter, TitleExtractor
    text_splitter = TokenTextSplitter(separator=" ", chunk_size=512, chunk_overlap=128)
    title_extractor = TitleExtractor(nodes=5)
    #Initilizing the pipeline with the transformations parameter
    pipeline = IngestionPipeline(transformations=[text_splitter, title_extractor])
    #Running the pipeline for storing the processed docuements in nodes
    nodes = pipeline.run(documents=docs, in_place=True, show_progress=True)

    #Conditional statements to check if the Directory exists or not
    if not os.path.exists(PERSIST_DIR):
        # Converting the nodes into indexes
        index = VectorStoreIndex(nodes)
        # If Directory does not exist then create one and store the index
        index.storage_context.persist(persist_dir=PERSIST_DIR)
    else:
        # Reloading the index. If any new file gets uploaded in the Google Drive Folder then the file can be indexed
        index = VectorStoreIndex(nodes)
        #storing the reloaded index
        index.storage_context.persist(persist_dir=PERSIST_DIR)
        # Loading the index from PERSIST_DIR
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context)
    return index