from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr, Field

# 같은 폴더에 있는 database.py와 models.py를 가져옵니다.
import database, models

# Pydantic 모델 (데이터 검증용)
class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    age: int | None = None

router = APIRouter()

@router.post("/create")
# get_db를 통해 DB 세션(db)을 받고, Pydantic 모델(user)로 데이터를 받습니다.
def create_user(user: User, db: Session = Depends(database.get_db)):
    # 1. Pydantic 모델을 SQLAlchemy 모델로 변환합니다.
    db_user = models.User(username=user.username, email=user.email, age=user.age)
    
    # 2. 데이터베이스 세션에 추가합니다. (아직 DB에 저장된 것 아님)
    db.add(db_user)
    
    # 3. 변경사항을 데이터베이스에 커밋(최종 저장)합니다.
    db.commit()
    
    # 4. 방금 저장한 데이터를 다시 읽어옵니다. (ID 등 생성된 값을 포함)
    db.refresh(db_user)
    
    # 5. 저장된 유저 정보를 반환합니다.
    return db_user


@router.put("/{user_id}")
def update_user(user_id: int, user: User):
    return {"user_id": user_id, "updated_to": user}

@router.delete("/{user_id}")
def delete_user(user_id: int):
    return {"status": "success", "message": f"User {user_id} has been deleted."}