# 1. 베이스 이미지 선택 (어떤 리눅스 + 파이썬 버전 위에서 시작할지)
FROM python:3.10-slim

# 2. 컨테이너 안의 작업 디렉토리 설정
WORKDIR /app

# 3. requirements.txt 파일 복사 및 라이브러리 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 현재 폴더의 모든 프로젝트 코드를 작업 디렉토리로 복사
COPY . .

# 5. 컨테이너가 시작될 때 실행될 최종 명령어
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8000"]