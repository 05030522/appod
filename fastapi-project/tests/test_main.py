import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

from main import app
from database import Base
from dependencies import get_db
import schemas

# 테스트마다 완전히 새로운 DB 파일 생성
TEST_DB_PATH = "./test_temp.db"
TEST_SQLALCHEMY_DATABASE_URL = f"sqlite:///{TEST_DB_PATH}"

# DB 세션 및 엔진 생성 (각 테스트마다 새로 만들도록 설정)
engine = create_engine(
    TEST_SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    future=True
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# DB 종속성 오버라이딩
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# pytest fixture로 테스트마다 완전한 초기화 수행
@pytest.fixture()
def client():
    # --- Setup ---
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)  # pytest 재실행 시 기존 DB 제거

    Base.metadata.create_all(bind=engine)
    test_client = TestClient(app)
    yield test_client

    # --- Teardown ---
    Base.metadata.drop_all(bind=engine)
    engine.dispose()
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)

# 실제 테스트 함수들
def test_create_user_success(client):
    response = client.post(
        "/users",
        json={"username": "testuser_success", "email": "success@example.com", "password": "testpassword"},
    )
    print("응답 상태:", response.status_code)
    print("응답 내용:", response.json())
    assert response.status_code == 200


def test_create_duplicate_user_fails(client):
    client.post(
        "/users",
        json={"username": "testuser_duplicate", "email": "duplicate@example.com", "password": "testpassword"},
    )
    response = client.post(
        "/users",
        json={"username": "testuser_duplicate", "email": "duplicate@example.com", "password": "testpassword"},
    )
    assert response.status_code == 400
