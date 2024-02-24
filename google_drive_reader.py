from llama_index.readers.google import GoogleDriveReader
loader = GoogleDriveReader()

def load_data(folder_id: str):
    docs = loader.load_data(folder_id=folder_id)
    # for doc in docs:
    #     doc.id_ = doc.metadata["file_name"]
    return docs

docs = load_data(folder_id="1cxqK_bHH5qdUrWSP8nx1s6_EwtFhcFRa")
