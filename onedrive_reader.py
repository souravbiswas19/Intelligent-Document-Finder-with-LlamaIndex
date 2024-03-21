from config import config
from instance_flag import old_file_id
from llama_index.readers.microsoft_onedrive import OneDriveReader

def read_onedrive():
    client_id = config["CLIENT_ID"]
    """
    This function reads the documents from the onedrive folder and returns a list of documents.
    """
    # User Authentication flow: Replace client id with your own id
    loader = OneDriveReader(client_id=client_id)
    documents = loader.load_data()
    for i in documents:
        old_file_id.add(i.id_)
    return documents