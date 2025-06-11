from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users" # 테이블의 이름

    # 테이블의 각 열(Column)을 정의합니다.
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    age = Column(Integer, nullable=True) # null을 허용