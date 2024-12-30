from pydantic import BaseModel,EmailStr 
from datetime import datetime
from typing import Optional
from pydantic.types import conint



class UserOut(BaseModel):
    #id:int
    email:EmailStr
    class Config:
        
        from_attributes=True
    
class PostBase(BaseModel):
    title: str
    content: str
    published: bool=True
    
    
class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    id:int
    created_at:datetime
    user_id:int
    owner:UserOut
    
    class Config:
        
        from_attributes=True
        
 
class post_vote(BaseModel):
    
    Post:PostResponse
    votes:int
    class Config:
       
        from_attributes=True
     
 
 
 
 
 
        
class UserCreate(BaseModel):
    email:EmailStr
    password:str
    



class UserLogin(BaseModel):
    email:EmailStr
    password:str
    
    
class Token(BaseModel):
    access_token:str
    token_type:str
    
class TokenData(BaseModel):
    id:Optional[int]=None
    
    
    
class Vote(BaseModel):
    
    post_id:int
    vote_dir:bool
    
    
