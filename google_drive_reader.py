"""This python module implements the access of files from the Google Drive Folder"""
from config import config
from instance_flag import old_file_id, new_file_id
from llama_index.readers.google import GoogleDriveReader

# Intialization of the Google Drive Loader
loader = GoogleDriveReader()

def load_data(folder_id: str):
    doc = loader.load_data(folder_id=folder_id)
    return doc

def load_new_data(old_docs, all_docs):
    for i in old_docs:
            old_file_id.add(i.id_)
    for i in all_docs:
        new_file_id.add(i.id_)
    unique_file_id = new_file_id.symmetric_difference(old_file_id)
    new_docs=[]
    for i in unique_file_id:
        for j in all_docs:
            if i == j.id_:
                new_docs.append(j)
    return new_docs

#Handling exception if folder cannot be accessed
try:    
    # load_data function is being called and list of documents is being stored
    print("Data Loading Started...")
    docs = load_data(folder_id=config['FOLDER_ID'])
    print("Loading Done")    
    # Printint the sucess message on success retrieval of data from folder
except Exception as e: # If folder cannot be accessed exception is raised
    print(f"Error occurred while loading data from Google Drive: {e}") # Prinitng the exception
    docs = None
