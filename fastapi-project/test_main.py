import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from main import app
from database import Base
from dependencies import get_db
import schemas

# --- 테스트용 DB 설정 (이전과 동일) ---
SQLALCHEMY_DATABASE_URL = "sqlite://"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db


@pytest.fixture()
def db_session():
    # 테스트 시작 전: 모든 테이블 생성
    Base.metadata.create_all(bind=engine)
    yield
    # 테스트 끝난 후: 모든 테이블 삭제
    Base.metadata.drop_all(bind=engine)
# ===============================

client = TestClient(app)

# --- 역할이 명확해진 테스트 함수들 ---

# 1. 사용자가 성공적으로 생성되는 경우만 테스트
def test_create_user_success(db_session): # fixture를 명시적으로 요청
    response = client.post(
        "/users",
        json={"username": "testuser", "email": "test@example.com", "password": "testpassword"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"
    assert "id" in data

# 2. 중복된 사용자를 생성하려 할 때 실패하는 경우만 테스트
def test_create_duplicate_user_fails(db_session): # fixture를 명시적으로 요청
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
    # 400 에러가 발생하는지 확인
    assert response.status_code == 400



# ===== 수정된 테스트 함수 =====
# def test_create_user():
#     # 1. 테스트 시작 전에 테이블을 만듭니다.
#     Base.metadata.create_all(bind=engine)
    
#     # 2. Arrange, Act, Assert (이전과 동일)
#     user_data = {
#         "username": "testuser2",
#         "email": "test2@example.com",
#         "password": "testpassword"
#     }
#     response = client.post("/users", json=user_data)
    
#     assert response.status_code == 200
#     data = response.json()
#     assert data["username"] == user_data["username"]
#     assert data["email"] == user_data["email"]
#     assert "id" in data
#     assert "password" not in data
    
#     # 3. 테스트가 끝난 후, 테이블을 모두 삭제하여 다음 테스트에 영향을 주지 않도록 합니다.
#     Base.metadata.drop_all(bind=engine)
# ===========================