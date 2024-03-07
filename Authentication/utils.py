import os
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Union, Any
import jwt
from decouple import config

ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_MINUTES = 600 * 24 * 7 # 7 days
ALGORITHM = config("ALGORITHM")
JWT_SECRET_KEY = config("JWT_SECRET_KEY")   # should be kept secret
#JWT_REFRESH_SECRET_KEY = config("JWT_REFRESH_SECRET_KEY") 

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def get_hashed_password(password: str) -> str:
    return password_context.hash(password)

def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)

def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
        
    else:
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
         
    
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
     
    return encoded_jwt
