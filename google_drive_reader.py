from config import config
from llama_index.readers.google import GoogleDriveReader
loader = GoogleDriveReader()

def load_data(folder_id: str):
    docs = loader.load_data(folder_id=folder_id)
    # for doc in docs:
    #     doc.id_ = doc.metadata["file_name"]
    return docs

docs = load_data(folder_id=config['FOLDER_ID'])
