from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from main import app
from database import Base
from dependencies import get_db

# 1. 테스트용 데이터베이스 설정 (메모리 DB 사용)
SQLALCHEMY_DATABASE_URL = "sqlite://" # In-memory SQLite database

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool, # 테스트용 설정
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# 2. 실제 DB 대신 테스트 DB를 사용하도록 의존성(dependency)을 오버라이드(override)합니다.
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db


# 3. 테스트 클라이언트 생성
client = TestClient(app)


# 4. 각 테스트가 실행되기 전에 DB 테이블을 생성합니다.
Base.metadata.create_all(bind=engine)



# ===== DB를 사용하는 API 테스트 ==
def test_create_user():
    # 1. 준비 (Arrange): API에 보낼 테스트용 데이터를 만듭니다.
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpassword"
    }
    
    # 2. 실행 (Act): /users 경로로 POST 요청을 보냅니다.
    response = client.post("/users", json=user_data)
    
    # 3. 검증 (Assert):
    # 응답 상태 코드가 200 (OK)인지 확인합니다.
    assert response.status_code == 200
    
    # 응답으로 받은 JSON 데이터를 확인합니다.
    data = response.json()
    assert data["username"] == user_data["username"]
    assert data["email"] == user_data["email"]
    # 응답에 id가 포함되어 있는지 확인합니다.
    assert "id" in data
    # 응답에 password 필드가 없는지 확인하여, 민감한 정보가 노출되지 않았는지 검증합니다
    assert "password" not in data