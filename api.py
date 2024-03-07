import os
import rag_query
from google_drive_reader import load_data
from store_vector_index import store_index
from check_folder import check_google_drive_folder
from fastapi import FastAPI, status, HTTPException



import Authentication.schemas as schemas
import Authentication.models as models
from datetime import datetime 
from Authentication.models import User
from Authentication.database import Base, SessionLocal, engine
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException,status
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
document=[]
app=FastAPI()

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
    #refresh = create_refresh_token(user.id)
    token_db = models.TokenTable(user_id=user.id,  access_token=access)
    db.add(token_db)
    db.commit()
    db.refresh(token_db)
    return {
        "access_token": access
    }

@app.post("/setlink", dependencies=[Depends(JWTBearer())], status_code=status.HTTP_202_ACCEPTED)
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

@app.post("/getquery", dependencies=[Depends(JWTBearer())], status_code=status.HTTP_202_ACCEPTED)
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
