from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
import database, models

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ===== 새로 추가된 가짜 유저 인증 함수 =====
def get_current_user(db: Session = Depends(get_db)):
    # 지금은 실제 로그인 기능이 없으므로,
    # DB에 있는 첫 번째 유저(id=1)를 항상 "로그인한 유저"라고 가정합니다.
    user = db.query(models.User).filter(models.User.id == 1).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User with id 1 not found. Please create it first.")
    return user