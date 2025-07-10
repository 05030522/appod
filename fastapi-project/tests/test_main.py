import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

from main import app
from database import Base
from dependencies import get_db
import schemas

# 1. 테스트용 DB 설정
TEST_SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(TEST_SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 2. 모든 준비와 정리를 책임지는 fixture
@pytest.fixture()
def client():
    # --- 테스트 시작 전 ---
    Base.metadata.create_all(bind=engine)
    
    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()
            
    app.dependency_overrides[get_db] = override_get_db
    
    yield TestClient(app)
    
    # --- 테스트 끝난 후 ---
    Base.metadata.drop_all(bind=engine)
    if os.path.exists("./test.db"):
        os.remove("./test.db")


def test_user_creation(client):
    """사용자 생성 성공 및 중복 생성 실패를 테스트합니다."""
    # 1. 첫 번째 사용자 생성 (성공 기대)
    response1 = client.post(
        "/users",
        json={"username": "testuser", "email": "test@example.com", "password": "testpassword"},
    )
    assert response1.status_code == 200, "User creation should be successful"
    data = response1.json()
    assert data["username"] == "testuser"
    assert "id" in data

    # 2. 중복된 username으로 생성 시도 (400 오류 기대)
    response2 = client.post(
        "/users",
        json={"username": "testuser", "email": "another@example.com", "password": "testpassword"},
    )
    assert response2.status_code == 400, "Duplicate username should fail"

    # 3. 중복된 email로 생성 시도 (400 오류 기대)
    response3 = client.post(
        "/users",
        json={"username": "anotheruser", "email": "test@example.com", "password": "testpassword"},
    )
    assert response3.status_code == 400, "Duplicate email should fail"



def test_create_post_after_login(client):
    """로그인한 사용자가 게시물을 생성하는지 테스트합니다."""
    # 준비 1: 사용자 생성
    user_data = {"username": "postuser", "email": "post@example.com", "password": "password123"}
    client.post("/users", json=user_data)
    
    # 준비 2: 생성한 사용자로 로그인하여 토큰 획득
    login_data = {"username": "postuser", "password": "password123"}
    login_response = client.post("/users/login", data=login_data)
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    # 실행: 토큰을 이용해 게시글 생성
    post_data = {"title": "My Test Post", "content": "This is a test."}
    response = client.post("/posts", json=post_data, headers=headers)
    
    # 검증
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "My Test Post"
    assert data["owner"]["username"] == "postuser"