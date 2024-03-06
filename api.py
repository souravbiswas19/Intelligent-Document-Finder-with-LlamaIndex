from fastapi import FastAPI

app = FastAPI()

@app.get("/getquery")
def getanswer():