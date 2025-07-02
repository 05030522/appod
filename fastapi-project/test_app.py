# tests/test_main.py

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


# 5. 여기에 새로운 테스트 함수들을 추가할 예정입니다.
def test_sample(): # 임시 테스트 함수
    assert 1 == 1