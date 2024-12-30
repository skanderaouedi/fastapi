from ..schema import UserCreate,UserOut
from .. import models 
from ..utils import hash_pass
from sqlalchemy.orm import Session 
from ..database import engine,get_db
from fastapi import status,HTTPException,Depends,APIRouter


router=APIRouter(
    prefix="/user",
    tags=["User"]
)
    
@router.post("", status_code=status.HTTP_201_CREATED,response_model=UserOut)
def create_user(user:UserCreate, db: Session = Depends(get_db) ) :
    #hash the password -user.password
    hashed_password=hash_pass(user.password)
    user.password=hashed_password
    #I NEED TO HANDLE WHEN THE EMAIL ALLREADY EXISIT
    try:
        new_user=models.User(**user.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as e:
        return {"error": str(e)+"this email is allready exisit"}


@router.get('/{id}',response_model=UserOut)
def get_user(id:int,db:Session=Depends(get_db)):
    user =db.query(models.User).filter(models.User.id==str(id)).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"hey this is id : {id} not found")
        
    else :
        print("hey this is the id: ", id , "this is your user you want ", user)
        
        
        return user