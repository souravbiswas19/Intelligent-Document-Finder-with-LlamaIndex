import os
import rag_query
import threading
from google_drive_reader import load_data, load_all_data
from store_vector_index import store_index
from onedrive_reader import read_onedrive
from check_folder import check_google_drive_folder, check_onedrive_folder
import Authentication.schemas as schemas
import Authentication.models as models
from Authentication.models import User
from Authentication.database import Base, SessionLocal, engine
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException,status, BackgroundTasks
from Authentication.auth_bearer import JWTBearer
from functools import wraps
from Authentication.utils import create_access_token, get_hashed_password, verify_password

Base.metadata.create_all(engine)
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

document_google=[]
document_onedrive=[]
app=FastAPI()

def start_check_google_drive_thread(docs):
    """
    This function starts a new thread to execute
    check_folder function infinitely.
    """
    threading.Timer(30, check_google_drive_folder, args=(docs,)).start()

def start_check_onedrive_thread(docs):
    """
    This function starts a new thread to execute
    check_folder2 function infinitely.
    """# Daemon thread so it automatically closes when the main thread (uvicorn server) exits
    threading.Timer(30, check_onedrive_folder, args=(docs,)).start()

@app.post("/register", status_code=status.HTTP_201_CREATED)
def register_user(user: schemas.UserCreate, session: Session = Depends(get_session)):
    existing_user = session.query(models.User).filter_by(email=user.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Email already registered")
    encrypted_password =get_hashed_password(user.password)
    new_user = models.User(username=user.username, email=user.email, password=encrypted_password )
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return {"message":"user created successfully"}

@app.post('/login' ,response_model=schemas.TokenSchema)
def login(request: schemas.Logindetails, db: Session = Depends(get_session), ):
    user = db.query(User).filter(User.email == request.email).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email")
    hashed_pass = user.password
    if not verify_password(request.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect password"
        )    
    access=create_access_token(user.id)
    token_db = models.TokenTable(user_id=user.id,  access_token=access)
    db.add(token_db)
    db.commit()
    db.refresh(token_db)
    return {
        "access_token": access
    }

# @app.post("/setlink", dependencies=[Depends(JWTBearer())], status_code=status.HTTP_202_ACCEPTED)
# def set_link(request: schemas.Link):
#     """Query the function version."""
#     format_google = "https://drive.google.com/drive/folders/"
#     folder_id = request.link[-(len(request.link)-len(format_google)):]
#     os.environ["FOLDER_ID"]=folder_id
#     try:
#         folder_id=os.getenv("FOLDER_ID")
#         print("Data loading Google Drive...")
#         docs = load_data(folder_id)
#         print("Data loading Done.")
#         document=docs
#         store_index(docs)
#         return {"Response": "Docs successfully loaded and Indexing done successfully"}
#     #Exception encountered if the pdf does not exist
#     except Exception as e:
#         raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e)) from e


@app.get("/getGoogleDriveData", dependencies=[Depends(JWTBearer())], status_code=status.HTTP_202_ACCEPTED)
def read_google_drive_data():
    """Query the function version."""
    try:
        docs = load_all_data()
        # backgroundtask.add_task(check_google_drive_folder(docs=document, folder_id=folder_id))
        #returns the answer after successful search from the pdf
        document_google=docs
        store_index(docs)
        return {"Response": "Docs successfully loaded from Google Drive and Indexing done successfully"}
    #Exception encountered if the pdf does not exist
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e)) from e
    
@app.get("/getOnedriveData", dependencies=[Depends(JWTBearer())], status_code=status.HTTP_202_ACCEPTED)
def read_onedrive_data():
    """Query the function version."""
    try:
        docs = read_onedrive()
        document_onedrive=docs
        store_index(docs)
        return {"Response": "Docs successfully loaded from OneDrive and Indexing done successfully"}
    #Exception encountered if the pdf does not exist
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e)) from e

@app.post("/getquery", dependencies=[Depends(JWTBearer())], status_code=status.HTTP_202_ACCEPTED)
def query(question: schemas.Question):
    """Query the function version."""
    background=BackgroundTasks()
    try:
        threading.Timer(0, start_check_google_drive_thread, args=(document_google,)).start()
        threading.Timer(0, start_check_onedrive_thread, args=(document_onedrive,)).start()
        # background.add_task(check_google_drive_folder(docs=document_google))
        # background.add_task(check_onedrive_folder(docs=document_onedrive))
        response = rag_query.generate_answer(question.question)
        #returns the answer after successful search from the pdf
        return {"answer": response}
    #Exception encountered if the pdf does not exist
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=str(e)) from e
