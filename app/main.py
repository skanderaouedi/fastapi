from fastapi import FastAPI
from .database import engine
from . import models 
from .routers import posts , users,auth,vote


"""  WE CAN  play with the response by passing a respons to the function def get x(id:int, response:Response)
resonse.status_code=400
"""
#we will use ORM SQLAlachny from now  as a ORM

models.base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)
@app.get("/")
def read_root():
    return {"Hello": "skander aouedi"}

   