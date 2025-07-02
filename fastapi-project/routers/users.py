from fastapi import APIRouter, Depends, HTTPException, status, Header, Path
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr, Field
from fastapi.security import OAuth2PasswordRequestForm
from dependencies import oauth2_scheme
from crud import crud_user

import database, models, auth, schemas, dependencies


router = APIRouter()


class TokenData(BaseModel):
    token: str


@router.get("/test-token")
def test_token(token: str = Depends(oauth2_scheme)):
    return {"token": token}



@router.post("", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    # DB에 이미 같은 이름의 유저가 있는지 확인
    db_user = crud_user.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    # 주방장에게 생성을 요청하고 결과를 바로 반환
    return crud_user.create_user(db=db, user=user)


@router.get("/{user_id}", response_model=schemas.UserResponse)
def read_user_by_id(user_id: int, db: Session = Depends(database.get_db)):
    # 주방장에게 조회를 요청
    db_user = crud_user.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
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


# ===== 최종 수정된 POST: 로그인 및 JWT 발급 =====
@router.post("/login", description="사용자 로그인 및 JWT 발급")
def login_for_access_token(
    # Pydantic 모델 대신, 다시 form_data를 사용합니다.
    form_data: OAuth2PasswordRequestForm = Depends(), 
    db: Session = Depends(database.get_db)
):
    # request.username 대신 form_data.username 으로 접근합니다.
    user = db.query(models.User).filter(models.User.username == form_data.username).first()

    # request.password 대신 form_data.password 로 접근합니다.
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = auth.create_access_token(
        data={"sub": user.username}
    )
    
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/test-token")
def test_token(token: str = Depends(oauth2_scheme)):
    return {"token": token}


# @router.get("/me", response_model=schemas.UserResponse)
# def read_users_me(current_user: models.User = Depends(dependencies.get_current_user)):
#     # 'get_current_user'가 반환한 사용자 객체를 그대로 리턴합니다.
#     return current_user


# @router.post("/test-token-manual")
# def test_token_manual(token_data: TokenData, db: Session = Depends(database.get_db)):
#     # 우리가 만든 예외를 그대로 사용
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials"
#     )
    
#     # auth.py의 토큰 검증 함수를 직접 호출
#     username = auth.verify_token(token_data.token, credentials_exception)
    
#     # 검증 성공 시 username 반환
#     return {"verified_username": username}