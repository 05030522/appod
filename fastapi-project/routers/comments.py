from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from dependencies import get_db, get_current_user

import database, models, schemas

router = APIRouter(
    prefix="/posts/{post_id}/comments",
    tags=["Comments"]
)


@router.post("", response_model=schemas.CommentResponse)
def create_comment(post_id: int, comment: schemas.CommentCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    db_comment = models.Comment(
         **comment.model_dump(),
        owner_id=current_user.id,
        post_id=post_id
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


@router.get("", response_model=list[schemas.CommentResponse])
def read_comments_for_post(post_id: int,
                            db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if post is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return post.comments


@router.put("/{comment_id}", response_model=schemas.CommentResponse)
def update_comment(comment_id: int,
                    comment_update: schemas.CommentUpdate,
                    db: Session = Depends(database.get_db),
                    current_user: models.User = Depends(get_current_user)):
    db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()

    if db_comment is None:
        raise HTTPException(status_code=404, detail="CommentPost not found")
    if db_comment.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this comment")
    update_data = comment_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_comment, key, value)
    db.commit()
    db.refresh(db_comment)
    return db_comment


@router.delete("/{comment_id}", status_code=204)
def delete_comment_by_id(comment_id: int,
                        db: Session = Depends(database.get_db),
                        current_user: models.User = Depends(get_current_user)):
    db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Post not found")
    if db_comment.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this post")
    db.delete(db_comment)
    db.commit()
    return