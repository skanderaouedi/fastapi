from .database import base 
from sqlalchemy import Column ,INTEGER,String,Boolean,ForeignKey
from  sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from  sqlalchemy.sql.sqltypes import TIMESTAMP

class Post(base):
    __tablename__="Posts"
    
    id=Column(INTEGER,primary_key=True,autoincrement=True,nullable=False)
    title=Column(String,nullable=False)
    content=Column(String,nullable=False)
    published=Column(Boolean,server_default="True",nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text("now()"))
    user_id=Column(INTEGER,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)
    
    owner=relationship("User")
    

class User(base):
    __tablename__="users"
    email=Column(String,nullable=False,unique=True)
    password=Column(String,nullable=False)
    id=Column(INTEGER,primary_key=True,autoincrement=True,nullable=False,unique=True)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text("now()"))
    
    
class Vote(base):
    __tablename__="votes"
    post_id=Column(INTEGER,ForeignKey("Posts.id",ondelete="CASCADE"),nullable=False,primary_key=True)
    user_id=Column(INTEGER,ForeignKey("users.id",ondelete="CASCADE"),nullable=False,primary_key=True)
    