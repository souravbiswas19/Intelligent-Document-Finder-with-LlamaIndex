from config import config
from llama_index.readers.microsoft_onedrive import OneDriveReader

def read_onedrive():
    client_id = config["CLIENT_ID"]
    """
    This function reads the documents from the onedrive folder and returns a list of documents.
    """
    # User Authentication flow: Replace client id with your own id
    loader = OneDriveReader(client_id=client_id)
    documents = loader.load_data()
    return documents