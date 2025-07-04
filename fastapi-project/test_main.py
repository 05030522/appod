import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
import os

from main import app
from database import Base
from dependencies import get_db

# --- 테스트용 DB 설정 (이전과 동일) ---
TEST_SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    TEST_SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False} # 이제 StaticPool은 필요 없습니다.
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture()
def client():
    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()
    
    app.dependency_overrides[get_db] = override_get_db
    Base.metadata.create_all(bind=engine)
    yield TestClient(app)
    Base.metadata.drop_all(bind=engine)


def test_create_user_success(client): # client fixture를 요청
    response = client.post(
        "/users",
        json={"username": "testuser", "email": "test@example.com", "password": "testpassword"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"

def test_create_duplicate_user_fails(client): # client fixture를 요청
    # 첫 번째 유저 생성
    client.post(
        "/users",
        json={"username": "testuser", "email": "test@example.com", "password": "testpassword"},
    )
    # 두 번째 중복 유저 생성 시도
    response = client.post(
        "/users",
        json={"username": "testuser", "email": "test@example.com", "password": "testpassword"},
    )
    assert response.status_code == 400