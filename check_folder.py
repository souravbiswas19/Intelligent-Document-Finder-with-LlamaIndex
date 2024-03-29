import os
#from config import config
from google_drive_reader import load_new_data, load_all_data
from onedrive_reader import read_onedrive
from gemini_llm import load_Gemini, load_embedding_model
from llama_index.core import StorageContext, load_index_from_storage, Settings
from llama_index.core.extractors import TitleExtractor
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.ingestion import IngestionPipeline

def check_google_drive_folder(docs):
    print("Google Drive Folder Checking Started...") # print statement before fetching Index
    # Loading the index from PERSIST_DIR
    """Function to store and return the index using VectorStoreIndex"""
    # Initializing the LLM model, embedding model and chunk size
    Settings.llm = load_Gemini()
    Settings.embed_model = load_embedding_model()
    Settings.chunk_size = 1024
    #Initializing TokenTextSplitter, TitleExtractor
    text_splitter = SentenceSplitter(separator="\n",chunk_size=1024, chunk_overlap=20)
    title_extractor = TitleExtractor(nodes=5)
    #Initilizing the pipeline with the transformations parameter
    pipeline = IngestionPipeline(transformations=[text_splitter, title_extractor, load_embedding_model()])
    #Running the pipeline for storing the processed docuements in nodes
    #Initializing the PERSISTENT DIRECTORY path
    PERSIST_DIR = "./storage"
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)
    all_docs = load_all_data()
    #finding the new files
    new_docs = load_new_data(docs, all_docs)
    # if new files are present then they are inserted into the index
    if new_docs:
        print("New Files found. Indexing Started...") # print statement before fetching Index
        new_nodes = pipeline.run(documents=new_docs, in_place=True, show_progress=True)
        index.insert_nodes(new_nodes)
        index.storage_context.persist(persist_dir=PERSIST_DIR)
    print("Folder Checking Successful.")

def check_onedrive_folder(docs):
    print("OneDrive Folder Checking Started...") # print statement before fetching Index
    # Loading the index from PERSIST_DIR
    """Function to store and return the index using VectorStoreIndex"""
    # Initializing the LLM model, embedding model and chunk size
    Settings.llm = load_Gemini()
    Settings.embed_model = load_embedding_model()
    Settings.chunk_size = 1024
    #Initializing TokenTextSplitter, TitleExtractor
    text_splitter = SentenceSplitter(separator="\n",chunk_size=1024, chunk_overlap=20)
    title_extractor = TitleExtractor(nodes=5)
    #Initilizing the pipeline with the transformations parameter
    pipeline = IngestionPipeline(transformations=[text_splitter, title_extractor, load_embedding_model()])
    #Running the pipeline for storing the processed docuements in nodes
    #Initializing the PERSISTENT DIRECTORY path
    PERSIST_DIR = "./storage"
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    index = load_index_from_storage(storage_context)
    all_docs = read_onedrive()
    #finding the new files
    new_docs = load_new_data(docs, all_docs)
    # if new files are present then they are inserted into the index
    if new_docs:
        print("New Files found. Indexing Started...") # print statement before fetching Index
        new_nodes = pipeline.run(documents=new_docs, in_place=True, show_progress=True)
        index.insert_nodes(new_nodes)
        index.storage_context.persist(persist_dir=PERSIST_DIR)
    print("Folder Checking Successful.")

