import os
import fastapi
a=0
app = fastapi.FastAPI()
@app.post("/set")
def set(link):
    os.environ["FOLDER"]=link
    a=0
    return "Successfully Set"

@app.get("/get")
def get():
    #folderid=os.getenv("FOLDER")
    return a