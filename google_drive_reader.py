"""This python module implements the access of files from the Google Drive Folder"""
from config import config
from llama_index.readers.google import GoogleDriveReader

# Intialization of the Google Drive Loader
loader = GoogleDriveReader()

def load_data(folder_id: str):
    """Function to load data from the 
    Google Drive Folder using the specified Folder ID"""
    doc = loader.load_data(folder_id=folder_id)
    # the list of documents is being returned
    return doc

# load_data function is being called and list of documents is being stored
docs = load_data(folder_id=config['FOLDER_ID'])
