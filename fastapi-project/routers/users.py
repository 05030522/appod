from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr, Field

# 같은 폴더에 있는 database.py와 models.py를 가져옵니다.
import database, models
import schemas
import auth

# Pydantic 모델 (데이터 검증용)
# class User(BaseModel):
#     username: str = Field(..., min_length=3, max_length=50)
#     email: EmailStr
#     age: int | None = None

# class UserResponse(BaseModel):
#     id: int
#     username: str
#     email: EmailStr
#     age: int | None

#     class Config:
#         orm_mode = True # SQLAlchemy

# class UserUpdate(BaseModel):
#     email: EmailStr | None = None
#     age: int | None = None

router = APIRouter()

@router.post("", response_model=schemas.UserResponse)
# get_db를 통해 DB 세션(db)을 받고, Pydantic 모델(user)로 데이터를 받습니다.
def create_user(user: schemas.User, db: Session = Depends(database.get_db)):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(username=user.username, email=user.email, age=user.age, hashed_password=hashed_password)
    

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/{user_id}")
def read_user_by_id(user_id: int, db: Session = Depends(database.get_db)):
    # DB에서 해당 ID를 가진 유저를 찾습니다.
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    
    # 만약 유저가 없다면, 404 에러를 발생시킵니다.
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # 유저가 있다면, 해당 유저 정보를 반환합니다.
    return db_user


@router.put("/{user_id}", response_model=schemas.UserResponse)
def update_user_by_id(user_id: int, user_update: schemas.UserUpdate, db: Session = Depends(database.get_db)):
    # 1. DB에서 수정할 유저를 찾습니다.
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # 2. Pydantic 모델에서 받은 데이터 중, 값이 있는 항목만 가져옵니다.
    update_data = user_update.model_dump(exclude_unset=True)
    
    # 3. 각 항목에 대해 db_user 객체의 값을 새로운 값으로 변경합니다.
    for key, value in update_data.items():
        setattr(db_user, key, value)
    
    # 4. 변경사항을 DB에 최종 저장합니다.
    db.commit()
    # 5. DB의 최신 정보로 객체를 갱신합니다.
    db.refresh(db_user)
    
    return db_user


@router.delete("/{user_id}", status_code=204)
def delete_user_by_id(user_id: int, db: Session = Depends(database.get_db)):
    # 1. 삭제할 유저를 찾습니다.
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # 2. DB 세션에서 해당 유저를 삭제 목록에 올립니다.
    db.delete(db_user)
    # 3. 변경사항을 DB에 최종 저장합니다.
    db.commit()
    
    # 내용 없이 204 응답만 보냅니다.
    return


@router.get("/{user_id}/posts", response_model=list[schemas.PostResponse])
def read_posts_by_user(user_id: int, db: Session = Depends(database.get_db)):
    # 1. 먼저 user_id로 유저를 찾습니다.
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # 2. user.posts를 통해 해당 유저의 모든 게시글을 반환합니다.
    return user.posts