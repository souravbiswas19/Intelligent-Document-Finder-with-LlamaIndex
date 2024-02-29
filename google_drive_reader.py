"""This python module implements the access of files from the Google Drive Folder"""
from config import config
from instance_flag import old_file_id, new_file_id
from llama_index.readers.google import GoogleDriveReader
# Intialization of the Google Drive Loader
loader = GoogleDriveReader()

def load_data(folder_id: str):
    """Function to load data from the Google Drive"""
    doc = loader.load_data(folder_id=folder_id)
    return doc

def load_new_data(old_docs, all_docs):
    """Function to separate out the new data from the Google Drive"""
    # Loop to store the unique id_ if each file of the old data
    for i in old_docs:
            old_file_id.add(i.id_)
    # Loop to store the unique id_ if each file of the new data
    for i in all_docs:
        new_file_id.add(i.id_)
    unique_file_id = new_file_id.symmetric_difference(old_file_id)
    # Extraction of the only new documents
    new_docs=[]
    # New documents id_ are being stored in a new list of Llama index documents
    for i in unique_file_id:
        for j in all_docs:
            if i == j.id_:
                new_docs.append(j)
    # To update the old file id with the newly added ones
    for i in unique_file_id:
        old_file_id.add(i)
    return new_docs # new files only returned

# Handling exception if folder cannot be accessed
try:    
    # load_data function is being called and list of documents is being stored
    print("Data Loading Started...") # print statement before loading the data
    docs = load_data(folder_id=config['FOLDER_ID'])
    print("Loading Done") # print statement after loading the data
    # Printint the sucess message on success retrieval of data from folder
except Exception as e: # If folder cannot be accessed exception is raised
    print(f"Error occurred while loading data from Google Drive: {e}") # Prinitng the exception
    docs = None
# End of File