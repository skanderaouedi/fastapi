from fastapi import FastAPI,Response,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
"""  WE CAN  play with the response by passing a respons to the function def get x(id:int, response:Response)
resonse.status_code=400
"""

#we will use ORM SQLAlachny from now on 
app = FastAPI()

class post(BaseModel):
    title: str
    content: str
    published: bool=True
    

while True:   
    try:
        conn = psycopg2.connect(database = "fastapi", 
                            user = "postgres", 
                            host= 'localhost',
                            password = "skander",
                            port = 5432,
                            cursor_factory=RealDictCursor)
    # Open a cursor to perform database operations
        cur = conn.cursor()
        print("database connection was seccessfully!")
        break
    except Exception as error :
        print("connection to die")
        print("Error: ", error)
        time.sleep(2)
   
  
my_posts=[{"title":"skander","content":"book","id":1},{"title":"aouedi","content":"books","id":2}]
@app.get("/")
def read_root():
    return {"Hello": "skander aouedi"}


@app.get("/posts")
def get_posts():
    cur.execute(""" SELECT * FROM public."Posts" """)
    posts=cur.fetchall()
    return {"data": posts}

#send a respont to front-end as we like

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: post ) :
    cur.execute(""" insert into public."Posts" (title,content,published) values (%s,%s,%s)  RETURNING * """,(post.title,
                post.content,post.published))
    new_post=cur.fetchone()
    conn.commit()
    return  new_post

import logging
#wher we pass a  id:int in the function we are making sure that the user will only can input an int
@app.get("/posts/{id}")
def get_post(id:int):
    logging.info(f"Received ID: {id}")
    #cur.execute(""" select * from  public."Posts"  where id=%s """,(str(id)))
    cur.execute("""SELECT * FROM public."Posts" WHERE id = %s""", (id,))
    post=cur.fetchone()
    print(post)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"hey this is id : {id} not found")
        
    else :
        print("hey this is the id: ", id , "this is your post: ", post)
        return post
          


@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    
    cur.execute(""" delete FROM public."Posts" WHERE id = %s returning*""" , (id,))
    post=cur.fetchone()
    print(post)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"hey this is id : {id} not found")
        
    else :
        print("hey this is the id: ", id , "this is your post you deleted: ", post)
        conn.commit()
        return post
    
@app.put("/posts/{id}")
def update_post(id:int,post:post):
    cur.execute(""" update public."Posts" set  title=%s, content=%s, published=%s WHERE id = %s returning * """ ,
                (post.title,post.content,post.published,str(id)))
    post=cur.fetchone()
    print(post)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"hey this is id : {id} not found")
        
    else :
        print("hey this is the id: ", id , "this is your post you deleted: ", post)
        conn.commit()
        return post