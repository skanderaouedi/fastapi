from datetime import datetime, timedelta
from jwt.exceptions import InvalidTokenError
import jwt 
from . import schema
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from datetime import datetime ,timedelta
from .config import settings


oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")
# to get a string like this run:
# openssl rand -hex 32

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes


def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    
    ENCODED_JWT=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return ENCODED_JWT

def verify_access_token(token:str,credentials_expception):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        id:str=payload.get("user_id")
        if id is None:
            raise credentials_expception
        token_data=schema.TokenData(id=id)
    except InvalidTokenError:
        raise credentials_expception
    return token_data
    
def get_current_user(token:str=Depends(oauth2_scheme)):
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials1",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return verify_access_token(token,credentials_exception)