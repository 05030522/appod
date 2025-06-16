from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone # datetime, timedelta, timezone 추가
from passlib.context import CryptContext

# ===== JWT 관련 설정 (파일 상단에 추가) =====
# 🚨 이 SECRET_KEY는 외부에 노출되면 안 됩니다.
# 실제 프로젝트에서는 .env 파일 등을 통해 환경 변수로 관리해야 합니다.
SECRET_KEY = "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# 1. 사용할 해싱 알고리즘과 설정을 정의합니다.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 2. 비밀번호를 해싱하는 함수
def get_password_hash(password: str):
    return pwd_context.hash(password)

# 3. 입력된 비밀번호와 해시된 비밀번호를 비교하는 함수
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


# ===== JWT 생성 함수 (파일 하단에 추가) =====
def create_access_token(data: dict):
    # 1. 복사본 생성: 원본 데이터를 변경하지 않기 위해 복사합니다.
    to_encode = data.copy()
    
    # 2. 만료 시간 설정: 현재 시간에 30분을 더해 만료 시간을 계산합니다.
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    # 3. JWT 인코딩: 데이터, 비밀 키, 알고리즘을 사용해 토큰을 생성합니다.
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt