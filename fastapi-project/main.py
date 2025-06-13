from fastapi import FastAPI
from routers import users, posts
from database import engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# '유저 부서(users.router)'를 본사(app)에 연결합니다.
app.include_router(users.router, prefix="/users", tags=["Users"])
# app.include_router(users.router, ...):
#   이 코드가 users.py에 있는 모든 API를 main.py의 app으로 가져와 포함시킵니다.
# prefix="/users": users.py에 있는 모든 API의 주소 앞에 /users를 자동으로 붙여줍니다.
# tags=["Users"]: /docs 자동문서에 'Users'라는 제목으로 API들을 그룹핑해주는 옵션입니다.
app.include_router(posts.router, prefix="/posts", tags=["Posts"])


# 본사에 남은 아이템 관련 API
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}