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

- **테스트 자동화:**
  - Pytest를 이용한 단위/통합 테스트 코드 작성
  - GitHub Actions를 통한 CI(지속적 통합) 파이프라인 구축.

## 3. 기술 스택

- **Backend:** Python 3.10, FastAPI, Pydantic, Uvicorn
- **Database:** PostgreSQL (운영), SQLite (로컬 개발), SQLAlchem (ORM)
- **Deployment & Infra:** AWS EC2, AWS S3, Docker, Gunicorn, PM2
- **Authentication:** JWT (python-jose), Passlib (with bcrypt)
- **Test & CI/CD:** Pytest, GitHub Actions

## 겪었던 문제 및 해결 과정

### 1. API 경로 순서 문제 (422 Error)

- **문제:** '내 정보 조회' API인 `GET /users/me` 요청이, '특정 유저 조회' API인 `GET /users/{user_id}`로 잘못 인식되어 `422 Unprocessable Content` 오류가 발생했습니다. FastAPI 라우터가 'me'를 `user_id`로 해석하려 했기 때문입니다.
- **해결:** FastAPI 라우터가 경로를 위에서부터 순차적으로 매칭한다는 원리를 파악하고, **'고정 경로'인 `/me`를 '변수 경로'인 `/{user_id}`보다 먼저 선언**하여 문제를 해결했습니다. 이를 통해 **RESTful API의 명확한 경로 설계**의 중요성을 체감했습니다.

### 2. 순환 참조 (Circular Import) 오류

- **문제:** `users` 라우터와 `posts` 라우터가 서로의 응답 모델(Pydantic 스키마)을 `import`하면서 순환 참조 오류가 발생하여 서버가 실행되지 않았습니다.
- **해결:** 모든 Pydantic 모델을 **`schemas.py`라는 별도의 공용 파일로 분리**하고, 각 라우터가 이 `schemas.py`만 참조하도록 의존성의 방향을 **중앙으로 모아 단방향으로 만들어** 문제를 해결했습니다. **'관심사 분리(SoC)'**와 의존성 관리의 중요성을 배웠습니다.

### 3. CI 환경에서의 환경 변수 누락 (ValidationError)

- **문제:** 로컬에서는 `.env` 파일로 잘 동작하던 테스트가, GitHub Actions 환경에서는 AWS 키를 찾지 못해 Pydantic `ValidationError`가 발생했습니다.
- **해결:** `.env`는 보안상 Git에 포함되지 않는다는 점을 인지하고, **GitHub Secrets**에 안전하게 키를 등록했습니다. 그 후, 워크플로우 파일(`ci.yml`)에서 `env` 키워드를 통해 이 Secret들을 **환경 변수로 주입**하여, CI 환경에서도 설정을 안전하게 불러올 수 있도록 구성했습니다.

## 4. 설치 및 실행 방법

### 1. 저장소 복제

```bash
git clone https://github.com/05030522/appod.git
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
