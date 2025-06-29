from dotenv import load_dotenv
import os

# 현재 파일(config.py)이 있는 폴더의 경로를 가져옵니다.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# .env 파일의 절대 경로를 만듭니다.
dotenv_path = os.path.join(BASE_DIR, ".env")

# .env 파일이 존재하는지 확인하고 로드합니다.
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
else:
    print("'.env' file not found. Please create it.")

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")