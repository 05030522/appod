from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    # .env 파일에서 읽어올 환경 변수들을 필드로 정의합니다.
    # 타입 힌트를 사용해 자동으로 형 변환 및 검증을 수행합니다.
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_REGION: str
    S3_BUCKET_NAME: str

    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    )

# 설정 클래스의 인스턴스를 생성합니다.
settings = Settings()