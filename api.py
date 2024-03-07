import rag_query
from fastapi import FastAPI, status, HTTPException

app = FastAPI()

@app.post("/getquery", status_code=status.HTTP_202_ACCEPTED)
async def query(question: str):
    """Query the function version."""
    try:
        response = rag_query.generate_answer(question)
        #returns the answer after successful search from the pdf
        return {"answer": response}
    #Exception encountered if the pdf does not exist
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e)) from e
