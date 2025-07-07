import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

from main import app
from database import Base
from dependencies import get_db
import schemas


SQLALCHEMY_DATABASE_URL = "sqlite:///./pytest.db"
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
    if os.path.exists("./pytest.db"): # DB 파일 삭제
        os.remove("./pytest.db")


def test_success(client):
    # 준비: 사용자 생성
    user_data = {"username": "testuser", "email": "test@example.com", "password": "testpassword"}
    client.post("/users", json=user_data)
    
    # 실행: 로그인
    login_data = {"username": "testuser", "password": "testpassword"}
    response = client.post("/users/login", data=login_data)
    
    try:
        assert response.status_code == 200
        print("✅ 상태 코드(200) 검증 성공")
    except AssertionError:
        print(f"❌ 상태 코드 검증 실패: 기대값=200, 실제값={response.status_code}")
        raise
    data = response.json()
    try:
        assert "access_token" in data
        print("✅ 액세스 토큰 존재 여부 검증 성공")
    except (AssertionError, KeyError): # JSON에 키가 없는 경우도 고려
        print("❌ 액세스 토큰 존재 여부 검증 실패")
        raise

    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    post_data = {"title": "Test Title", "content": "Test Content"}
    response = client.post("/posts", json=post_data, headers=headers)
    try:
        assert response.status_code == 200
        print("✅ 게시글 생성 상태 코드(200) 검증 성공")
    except AssertionError:
        print(f"❌ 게시글 생성 상태 코드 검증 실패: 기대값=200, 실제값={response.status_code}")
        print("하아~ 짜증난다~ 와 안되고 그라노~")
        raise


# def test_post_lifecycle(client):
#     --- 1. 준비 (Arrange): 모든 단계를 검증합니다. ---
    
#     # 사용자 A 생성 및 성공 검증
#     user_a_data = {"username": "user_a1", "email": "a123@test.com", "password": "password123"}
#     response = client.post("/users", json=user_a_data)
#     assert response.status_code == 200, f"사용자 A 생성 실패: {response.json()}"

#     # 사용자 B 생성 및 성공 검증
#     user_b_data = {"username": "user_b2", "email": "b123@test.com", "password": "password12"}
#     response = client.post("/users", json=user_b_data)
#     assert response.status_code == 200, f"사용자 B 생성 실패: {response.json()}"

#     # 사용자 A로 로그인 및 성공 검증
#     login_data_a = {"username": "user_a1", "password": "password123"}
#     login_res_a = client.post("/users/login", data=login_data_a)
#     assert login_res_a.status_code == 200, f"사용자 A 로그인 실패: {login_res_a.json()}"
#     token_a = login_res_a.json()["access_token"]
#     headers_a = {"Authorization": f"Bearer {token_a}"}

#     # 사용자 B로 로그인 및 성공 검증
#     login_data_b = {"username": "user_b2", "password": "password12"}
#     login_res_b = client.post("/users/login", data=login_data_b)
#     assert login_res_b.status_code == 200, f"사용자 B 로그인 실패: {login_res_b.json()}"
#     token_b = login_res_b.json()["access_token"]
#     headers_b = {"Authorization": f"Bearer {token_b}"}


#     # --- 2. 게시글 생성 (Act & Assert) ---
#     post_data = {"title": "Test Title", "content": "Test Content"}
#     response = client.post("/posts", json=post_data, headers=headers_a) # A가 글 작성
    
#     assert response.status_code == 200
#     created_post = response.json()
#     post_id = created_post["id"]

#     # ... (이하 수정/삭제 테스트는 동일) ...
#     # 성공 케이스: A가 자기 글을 수정
#     response = client.put(f"/posts/{post_id}", json={"title": "Updated"}, headers=headers_a)
#     assert response.status_code == 200

#     # 실패 케이스: B가 A의 글을 삭제 시도
#     response = client.delete(f"/posts/{post_id}", headers=headers_b)
#     assert response.status_code == 403

#     # 성공 케이스: A가 자기 글을 삭제
#     response = client.delete(f"/posts/{post_id}", headers=headers_a)
#     assert response.status_code == 204