import os
import rag_query
from google_drive_reader import load_data
from store_vector_index import store_index
from check_folder import check_google_drive_folder
from fastapi import FastAPI, status, HTTPException

app = FastAPI()
document=[]
@app.post("/setlink", status_code=status.HTTP_202_ACCEPTED)
def set_link(link: str):
    """Query the function version."""
    format_google = "https://drive.google.com/drive/folders/"
    folder_id = link[-(len(link)-len(format_google)):]
    os.environ["FOLDER_ID"]=folder_id
    try:
        folder_id=os.getenv("FOLDER_ID")
        docs = load_data(folder_id)
        document=docs
        store_index(folder_id, docs)
        return {"Response": "Docs successfully loaded and Indexing done successfully"}
    #Exception encountered if the pdf does not exist
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e)) from e

@app.post("/getquery", status_code=status.HTTP_202_ACCEPTED)
def query(question: str):
    """Query the function version."""
    try:
        folder_id=os.getenv("FOLDER_ID")
        print(folder_id)
        check_google_drive_folder(docs=document, folder_id=folder_id)
        response = rag_query.generate_answer(question,folder_id)
        #returns the answer after successful search from the pdf
        return {"answer": response}
    #Exception encountered if the pdf does not exist
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e)) from e
