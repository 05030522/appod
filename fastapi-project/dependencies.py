from fastapi import Request, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
import database, models, auth

# ===== OAuth2 설정 =====
# "/users/login" API 경로에서 토큰을 받아오겠다고 설정합니다.
# 이 부분이 /docs의 Authorize 버튼 동작 방식에 영향을 줍니다.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")
# =====================

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# get_current_user 함수입니다.
def get_current_user(
    token: str = Depends(oauth2_scheme), 
    db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    username = auth.verify_token(token, credentials_exception)
    
    user = db.query(models.User).filter(models.User.username == username).first()
    
    if user is None:
        raise credentials_exception
        
    return user