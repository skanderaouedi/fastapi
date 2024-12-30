from .. import models 
from ..schema import PostCreate, PostResponse,Vote
from sqlalchemy.orm import Session 
from typing import List,Optional
from ..database import get_db
from .. import oauth2
from fastapi import status,HTTPException,Depends,APIRouter


router=APIRouter(
    prefix="/vote",
    tags=["votes"]
)

@router.post("/",status_code=status.HTTP_201_CREATED)
def vote(vote:Vote,db:Session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    
    check_post=db.query(models.Post).filter(models.Post.id==vote.post_id).first()
    if not check_post :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="hey this post doesn't exisit")
    
    vote_query=db.query(models.Vote).filter(models.Vote.post_id==vote.post_id,models.Vote.user_id==current_user.id)
    found_vote=vote_query.first()
    if vote.vote_dir:
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"user{current_user.id} has allready liked the post")
        new_vote= models.Vote(post_id=vote.post_id,user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message":"hey the vote is made"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="vote does not exsist")
        vote_query.delete(synchronize_session=False)
        return{"message":"hey vote deleted"}