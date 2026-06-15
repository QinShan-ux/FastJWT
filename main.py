from typing import Annotated

from fastapi import FastAPI, Depends, HTTPException
from fastapi.openapi.utils import get_openapi
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel,Field
from starlette import status
from tortoise.contrib.fastapi import register_tortoise
from apps.core.security import get_current_user,login
from apps.routers import teacherRouter

from settings import TORTOISE_ORM
from apps.middlewares import register_custom_middleware



class Login(BaseModel):
    account: str = Field(default="linan")
    password: str = Field(default="1234")
    type:str = Field(default="teacher")

class Token(BaseModel):
    access_token: str
    token_type: str


app = FastAPI()

# 注册路由
app.include_router(teacherRouter.router)
# 注册中间件
register_custom_middleware(app)

# 该方法会在fastapi启动时触发，内部通过传递进去的app对象，监听服务启动和终止事件
# 当检测到启动事件时，会初始化Tortoise对象，如果generate_schemas为True则还会进行数据库迁移
# 当检测到终止事件时，会关闭连接
register_tortoise(
    app,
    #数据库配置信息
    config=TORTOISE_ORM,
    # generate_schemas=True,  # 如果数据库为空，则自动生成对应表单，生产环境不要开
    # add_exception_handlers=True,  # 生产环境不要开，会泄露调试信息
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/token")
async def login_for_access_token(
    form_data:  Login,
) -> Token:
    access_token = await login(form_data.account, form_data.password,form_data.type)
    return Token(access_token="Bearer " + access_token, token_type="bearer")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)