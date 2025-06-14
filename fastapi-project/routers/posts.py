from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr, Field
from dependencies import get_current_user
import database, models

class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True # SQLAlchemy


class PostUpdate(PostBase):
    title: str  | None = None
    content: str  | None = None

        
router = APIRouter()


@router.post("", response_model=PostResponse)
def create_post(post: PostCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    db_post = models.Post( **post.model_dump(), owner_id=current_user.id)  # ** < 이 부분 딕셔너리 언패킹(Dictionary Unpacking)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

@router.get("/allposts", response_model=list[PostResponse])
def all_post(db: Session = Depends(database.get_db)):
    db_posts = db.query(models.Post).all()
    return db_posts

@router.get("/{post_id}", response_model=PostResponse)
def read_post(post_id: int, db: Session = Depends(database.get_db)):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_post

@router.put("/{post_id}", response_model=PostResponse)
def update_post(post_id: int, post_update: PostUpdate, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()

    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    if db_post.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this post")
    update_post = post_update.model_dump(exclude_unset=True)

    for key, value in update_post.items():
        setattr(db_post, key, value)
    db.commit()
    db.refresh(db_post)
    return db_post

@router.delete("/{post_id}", status_code=204)
def delete_post_by_id(post_id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    if db_post.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this post")
    db.delete(db_post)
    db.commit()
    return