"""
This python module performs the function of storing 
the vectors along with the implementation of TitleExtractor
"""
#importing the necessary libraries
import os
from instance_flag import old_file_id
from gemini_llm import load_Gemini, load_embedding_model
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage, Settings
from llama_index.core.extractors import TitleExtractor
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.ingestion import IngestionPipeline
# Error Handling during storing of indexes
try:
    def load_index():
        PERSIST_DIR = "./storage"
        Settings.embed_model = load_embedding_model()
        print("Index Loading Started...") # print statement before fetching Index
        # Loading the index from PERSIST_DIR
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context)
        print("Index Loading Done")
        return index
    
    def store_index(document):
        """Fucntion to store and return the index using VectorStoreIndex"""
        #Initializing the LLM model, embedding model and chunk size
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
        #Conditional statements to check if the Directory exists or not
        if not os.path.exists(PERSIST_DIR):
            # Converting the nodes into indexes
            print("Indexing of Nodes started...")
            nodes = pipeline.run(documents=document, in_place=True, show_progress=True)
            index = VectorStoreIndex(nodes,show_progress=True)
            # If Directory does not exist then create one and store the index
            index.storage_context.persist(persist_dir=PERSIST_DIR)
            for i in document:
                old_file_id.add(i.id_)
            print("Indexing of node done successfully.")
        else:
            # Reloading the index. If any new file gets uploaded in the Google Drive Folder then the file can be indexed
            #storing the reloaded index
            print("Index Checking Started...") # print statement before fetching Index
            # Loading the index from PERSIST_DIR
            # nodes = pipeline.run(documents=document, in_place=True, show_progress=True)
            # index = VectorStoreIndex(nodes,show_progress=True)
            # If Directory does not exist then create one and store the index
            # index.storage_context.persist(persist_dir=PERSIST_DIR)
            for i in document:
                old_file_id.add(i.id_)
            storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
            index = load_index_from_storage(storage_context)
            print("Index Checking Successful.")
        return index
except Exception as e:
    # Error handling during indexing
    print(f"Error occurred while storing the index: {e}")
# End of File