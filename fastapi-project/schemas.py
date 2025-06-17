from pydantic import BaseModel, EmailStr, Field

# User 관련 모델들
class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str
    age: int | None = None

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    age: int | None

    class Config:
        orm_mode = True # SQLAlchemy

class UserUpdate(BaseModel):
    email: EmailStr | None = None
    age: int | None = None

# Post 관련 모델들
class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass # 나중에 owner_id를 여기서 받을 수도 있습니다.

class PostResponse(PostBase):
    id: int
    owner_id: int
    owner: UserResponse # UserResponse를 그대로 사용
    class Config:
        orm_mode = True

class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    owner_id: int
    owner: UserResponse

    class Config:
        orm_mode = True # SQLAlchemy

class PostUpdate(PostBase):
    title: str  | None = None
    content: str  | None = None


class TokenRequest(BaseModel):
    username: str
    password: str