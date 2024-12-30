from fastapi import status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session 
from ..database import get_db
from .. import models 
from ..schema import Token
from ..utils import verify_password
from ..oauth2 import create_access_token
from fastapi.security.oauth2 import OAuth2PasswordRequestForm



router=APIRouter(
    tags=["Authentication"]
)

@router.post("/login",response_model=Token)
def login(user_credentails:OAuth2PasswordRequestForm=Depends(),db: Session=Depends(get_db)):
    
    user_Data=db.query(models.User).filter(models.User.email==user_credentails.username).first()
    
    if not user_Data:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"Invalide Credentials")
    if not verify_password(user_credentails.password,user_Data.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"Invalide Credentials1")
        
    else:
        #in the function you pass the payload that you want to create the token header,payload 
        access_token=create_access_token(data={"user_id":user_Data.id})
        return {"access_token":access_token,"token_type":"bearer"}
            