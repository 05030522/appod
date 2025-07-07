import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

from main import app
from database import Base
from dependencies import get_db
import schemas


SQLALCHEMY_DATABASE_URL = "sqlite:///./test2.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture()
def client():
    # --- 테스트 시작 전 ---
    Base.metadata.create_all(bind=engine) # 테이블 생성
    yield TestClient(app)
    # --- 테스트 끝난 후 ---
    Base.metadata.drop_all(bind=engine) # 테이블 삭제
    engine.dispose()
    if os.path.exists("./test2.db"): # DB 파일 삭제
        os.remove("./test2.db")

def test_login_success(client):
    # 준비: 사용자 생성
    user_data = {"username": "testuser", "email": "test@example.com", "password": "testpassword"}
    client.post("/users", json=user_data)
    
    # 실행: 로그인
    login_data = {"username": "testuser", "password": "testpassword"}
    response = client.post("/users/login", data=login_data)
    
    # 검증
    assert response.status_code == 200
    assert "access_token" in response.json()