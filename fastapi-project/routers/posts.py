from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import get_current_user

import database, models, schemas

router = APIRouter()


@router.post("", response_model=schemas.PostResponse)
def create_post(post: schemas.PostCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    db_post = models.Post( **post.model_dump(), owner_id=current_user.id)  # ** < 이 부분 딕셔너리 언패킹(Dictionary Unpacking)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

@router.get("", response_model=list[schemas.PostResponse])
def all_post(skip: int = 0,
            limit: int = 10,
            db: Session = Depends(database.get_db)
            ):
    db_posts = db.query(models.Post).offset(skip).limit(limit).all()
    return db_posts

@router.get("/{post_id}", response_model=schemas.PostResponse)
def read_post(post_id: int, db: Session = Depends(database.get_db)):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_post

@router.put("/{post_id}", response_model=schemas.PostResponse)
def update_post(post_id: int, post_update: schemas.PostUpdate, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
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