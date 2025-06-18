# schemas.py (수정 최종안)

from pydantic import BaseModel, EmailStr

# --- User Schemas ---
class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str # 생성 시에만 비밀번호를 받음

class UserUpdate(BaseModel):
    email: EmailStr | None = None
    age: int | None = None

class UserResponse(UserBase):
    id: int
    age: int | None = None
    class Config:
        orm_mode = True

# --- Post Schemas ---
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
        orm_mode = True

class PostUpdate(BaseModel):
    title: str | None = None
    content: str | None = None

# (TokenRequest는 그대로 두셔도 좋습니다)
class TokenRequest(BaseModel):
    username: str
    password: str


class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    pass

class CommentResponse(CommentBase):
    id: int
    owner_id: int
    post_id: int
    owner: UserResponse # 댓글 작성자 정보 포함

    class Config:
        # Pydantic V2부터는 orm_mode 대신 from_attributes 입니다.
        # 둘 다 써도 경고만 뜰 뿐 문제는 없습니다.
        from_attributes = True


class CommentUpdate(BaseModel):
    content: str | None = None