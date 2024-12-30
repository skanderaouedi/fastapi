from .. import models 
from ..schema import PostCreate, PostResponse,post_vote
from sqlalchemy.orm import Session 
from typing import List,Optional,Dict
from ..database import get_db
from .. import oauth2
from fastapi import status,HTTPException,Depends,APIRouter
from sqlalchemy import func

router=APIRouter(
    prefix="/post",
    tags=["Posts"]
)
@router.get("",response_model=List[post_vote])
def get_posts(db: Session = Depends(get_db),user_id:int=Depends(oauth2.get_current_user),limit:int=10,skip:int=0,
            search:Optional[str]="" ):
    
    
    
    try:
        
        

        
        posts = (
            db.query(
                models.Post,
                func.count(models.Vote.post_id).label("votes")
            )
            .join(models.Vote, models.Post.id == models.Vote.post_id, isouter=True)
            .group_by(models.Post.id).filter(models.Post.title.contains(search))
            .limit(limit)
            .offset(skip)
            .all()
        )
      
       
        return posts
    except Exception as e:
        return {"error": str(e)}
    

#send a respont to front-end as we like
@router.post("", status_code=status.HTTP_201_CREATED,response_model=PostResponse)
def create_posts(post:PostCreate, db: Session = Depends(get_db) ,current_user:int=Depends(oauth2.get_current_user)) :
    print(current_user)
    new_post=models.Post(user_id=current_user.id,**post.dict())
    print(new_post)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


#wher we pass a  id:int in the function we are making sure that the user will only can input an int
@router.get("/{id}",response_model=post_vote)
def get_post(id:int,db: Session = Depends(get_db),user_id:int=Depends(oauth2.get_current_user)):
    
    
    post=db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Post.id == models.Vote.post_id, isouter=True).group_by(models.Post.id).filter(models.Post.id==id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"hey this is id : {id} not found")
        
    else : 
              
        print("hey this is the id: ", id , "this is your post: ", post)
        return post
    
    
    
@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db: Session = Depends(get_db),user_id:int=Depends(oauth2.get_current_user)):

    post_query=db.query(models.Post).filter(models.Post.id==id)
    if post_query.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"hey this is id : {id} not found")
    post=post_query.first()  
    print(id, "hey thi sis the user id",post.user_id, "hey this is the userid",user_id.id)  
    if post.user_id!= user_id.id :
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"hey  you can't delete this post")
    else:
        post_query.delete(synchronize_session=False)
        db.commit()
        return post    

@router.put("/{id}",response_model=PostResponse)
def update_post(id:int,update_post:PostCreate,db: Session = Depends(get_db),user_id:int=Depends(oauth2.get_current_user)):
    
    post_query=db.query(models.Post).filter(models.Post.id==id)
    
    post=post_query.first()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"hey this is id : {id} not found")
    
    if post.user_id!=user_id.id :
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"hey  you can't update this post")
        
    else :
        print("hey this is the id: ", id , "this is the post you updated: ", post)
        post_query.update(update_post.dict(),synchronize_session=False)
        db.commit()
        
        return post_query.first()