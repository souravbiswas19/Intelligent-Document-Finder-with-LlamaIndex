"""
This python module performs the function of storing 
the vectors along with the implementation of TitleExtractor
"""
#importing the necessary libraries
import os
from config import config
from google_drive_reader import docs, load_data, load_new_data
from gemini_llm import llm, embed_model
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage, Settings
from llama_index.core.extractors import TitleExtractor
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.ingestion import IngestionPipeline
try:
    def store_index():    
        #Initializing the LLM model, embedding model and chunk size
        Settings.llm = llm
        Settings.embed_model = embed_model
        Settings.chunk_size = 1024    
        #Initializing TokenTextSplitter, TitleExtractor
        text_splitter = SentenceSplitter(separator="\n",chunk_size=1024, chunk_overlap=20)
        title_extractor = TitleExtractor(nodes=5)
        #Initilizing the pipeline with the transformations parameter
        pipeline = IngestionPipeline(transformations=[text_splitter, title_extractor])
        #Running the pipeline for storing the processed docuements in nodes
        #Initializing the PERSISTENT DIRECTORY path
        PERSIST_DIR = "./storage"
        #Conditional statements to check if the Directory exists or not
        if not os.path.exists(PERSIST_DIR):
            # Converting the nodes into indexes
            nodes = pipeline.run(documents=docs, in_place=True, show_progress=True)
            index = VectorStoreIndex(nodes,show_progress=True)
            # If Directory does not exist then create one and store the index
            index.storage_context.persist(persist_dir=PERSIST_DIR)
            print("Indexing done successfully")
        else:
            # Reloading the index. If any new file gets uploaded in the Google Drive Folder then the file can be indexed
            # index = VectorStoreIndex(nodes, show_progress=True)
            #storing the reloaded index
            # index.storage_context.persist(persist_dir=PERSIST_DIR)
            print("Index Checking Started...")
            # Loading the index from PERSIST_DIR
            storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
            index = load_index_from_storage(storage_context)
            all_docs = load_data(folder_id=config['FOLDER_ID'])
            new_docs = load_new_data(docs, all_docs)
            if new_docs:
                new_nodes = pipeline.run(documents=new_docs, in_place=True, show_progress=True)
                index.insert_nodes(new_nodes)
            print("Index Checking Successful")
        return index
except Exception as e:
    # Error handling during indexing
    print(f"Error occurred while storing the index: {e}")