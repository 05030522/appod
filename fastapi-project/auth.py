from passlib.context import CryptContext

# 1. 사용할 해싱 알고리즘과 설정을 정의합니다.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 2. 비밀번호를 해싱하는 함수
def get_password_hash(password: str):
    return pwd_context.hash(password)

# 3. 입력된 비밀번호와 해시된 비밀번호를 비교하는 함수
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)