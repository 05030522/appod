import boto3
import config 
from fastapi import APIRouter, Depends, UploadFile, File

router = APIRouter(
    prefix="/uploads",
    tags=["Uploads"]
)

# # S3 클라이언트 생성
# s3 = boto3.client(
#     's3',
#     aws_access_key_id=config.AWS_ACCESS_KEY_ID,
#     aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
#     region_name=config.AWS_REGION
# )
# BUCKET_NAME = config.S3_BUCKET_NAME

# S3 클라이언트 생성 부분 수정
s3 = boto3.client(
    's3',
    aws_access_key_id=config.settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=config.settings.AWS_SECRET_ACCESS_KEY,
    region_name=config.settings.AWS_REGION
)
BUCKET_NAME = config.settings.S3_BUCKET_NAME

@router.post("/image")
async def upload_image(file: UploadFile = File(...)):
    # S3에 파일 업로드
    s3.upload_fileobj(
        file.file, # 업로드할 파일 객체
        BUCKET_NAME, # 버킷 이름
        file.filename, # S3에 저장될 파일 이름
        ExtraArgs={'ContentType': file.content_type} # 파일의 콘텐츠 타입(MIME 타입)
    )
    
    # 업로드된 파일의 URL 생성
    # file_url = f"https://{BUCKET_NAME}.s3.{config.AWS_REGION}.amazonaws.com/{file.filename}"
    file_url = f"https://{BUCKET_NAME}.s3.{config.settings.AWS_REGION}.amazonaws.com/{file.filename}"
    
    return {"file_url": file_url}