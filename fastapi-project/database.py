from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# 사용할 데이터베이스를 설정합니다. 여기서는 SQLite를 사용합니다.
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# 데이터베이스와 통신하는 엔진을 만듭니다.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 데이터베이스와 대화할 세션(통로)을 만드는 공장입니다.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 모든 DB 모델들이 상속받을 기본 클래스입니다.
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
