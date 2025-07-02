# FastAPI 기반 웹 서비스 프로젝트

## 1. 프로젝트 소개

이 프로젝트는 Python의 현대적인 웹 프레임워크인 **FastAPI**를 학습하고, 백엔드 개발의 전체 사이클을 경험하기 위해 만들어졌습니다.

단순한 API 개발을 넘어, 데이터베이스 연동, 사용자 인증, 클라우드 배포 및 컨테이너화까지 실제 서비스를 운영하는 데 필요한 핵심적인 기술들을 종합적으로 다루는 것을 목표로 합니다.

## 2. 주요 기능

- **사용자 관리 (CRUD):**

  - JWT를 이용한 회원가입, 로그인, 인증
  - 비밀번호는 bcrypt로 안전하게 해싱하여 저장

- **게시글 관리 (CRUD):**

  - 로그인한 사용자만 게시글 생성 가능
  - 소유권 기반으로 수정/삭제 권한 관리

- **댓글 관리 (CRUD):**

  - 특정 게시글에 댓글 생성/조회/수정/삭제
  - 소유권 기반 권한 관리 적용

- **파일 업로드:**

  - AWS S3와 연동하여 이미지 등 정적 파일 업로드
  - 업로드된 파일의 URL 관리

- **페이지네이션 및 정렬:**

  - 대량 데이터를 효율적으로 조회하기 위한 `skip`, `limit`, 정렬 기능 구현

- **클라우드 배포:**

  - Docker 컨테이너 기술로 AWS EC2 인스턴스에 배포
  - Gunicorn과 PM2를 통해 무중단 운영 가능

## 3. 기술 스택

- **Backend:** Python 3.10, FastAPI, Pydantic, Uvicorn
- **Database:** PostgreSQL (운영), SQLite (로컬 개발), SQLAlchemy (ORM)
- **Deployment & Infra:** AWS EC2, AWS S3, Docker, Gunicorn, PM2
- **Authentication:** JWT (python-jose), Passlib (with bcrypt)

## 4. 설치 및 실행 방법

### 1. 저장소 복제

```bash
git clone https://github.com/your-username/fastapi-project.git
cd fastapi-project
```

### 2. 가상환경 생성 및 활성화

```bash
# Unix/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
.\venv\Scripts\activate
```

### 3. 필요 라이브러리 설치

```bash
pip install -r requirements.txt
```

### 4. .env 파일 설정

프로젝트 루트 디렉토리에 `.env` 파일을 생성하고 아래와 같이 입력합니다:

```
AWS_ACCESS_KEY_ID=YOUR_AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY=YOUR_AWS_SECRET_ACCESS_KEY
AWS_REGION=ap-northeast-2
S3_BUCKET_NAME=your-unique-s3-bucket-name
```

### 5. 로컬 서버 실행

```bash
uvicorn main:app --reload
```

서버 실행 후, 웹 브라우저에서 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) 로 접속하여 API 문서를 확인할 수 있습니다.

## 5. API 엔드포인트

| Method | Path                        | 설명                    | 인증 필요 |
| ------ | --------------------------- | ----------------------- | --------- |
| POST   | `/users`                    | 회원가입                | ✕         |
| POST   | `/login`                    | 로그인 (JWT 발급)       | ✕         |
| GET    | `/users/me`                 | 내 정보 조회            | ✔         |
| POST   | `/posts/{post_id}/comments` | 특정 게시글에 댓글 작성 | ✔         |
| GET    | `/posts`                    | 게시글 목록 조회        | ✕         |
| GET    | `/posts/{post_id}`          | 특정 게시글 조회        | ✕         |
| PUT    | `/posts/{post_id}`          | 게시글 수정             | ✔ (본인)  |
| DELETE | `/posts/{post_id}`          | 게시글 삭제             | ✔ (본인)  |
| POST   | `/uploads/image`            | 이미지 업로드           | ✔         |
