from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from datetime import timedelta, datetime, timezone
import jwt
from jwt import PyJWTError
from fastapi.security import APIKeyHeader

from apps.model.student import Student
from apps.model.teacher import Teacher
from pwdlib import PasswordHash

# ==================== 配置 ====================
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

api_key_header = APIKeyHeader(name="Authorization", auto_error=False)
pwd_hasher = PasswordHash.recommended()


# ==================== 核心依赖 ====================
async def get_current_user(authorization: Annotated[str | None, Depends(api_key_header)]):
    """
    验证 JWT Token 并返回当前用户信息
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    # 1. 检查 Header 是否存在
    if not authorization:
        raise credentials_exception

    # 2. 提取 Bearer token
    # 格式: "Bearer <token>" 或 "<token>"
    parts = authorization.split()
    if len(parts) == 2 and parts[0].lower() == "bearer":
        token = parts[1]
    elif len(parts) == 1:
        token = parts[0]
    else:
        raise credentials_exception

    try:
        # jwt.decode 会自动验证 exp 过期时间，无需手动检查
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("username")
        role: str = payload.get("role")

        if username is None or role is None:
            raise credentials_exception

    except PyJWTError:
        raise credentials_exception

    # 从数据库查询真实用户信息
    user = await get_user_from_db(username, role)
    if user is None or user.get("disabled"):
        raise credentials_exception

    # 返回真实用户数据（修复：原代码返回了硬编码的假数据）
    return user


async def get_current_active_user(
    user: dict = Depends(get_current_user)
):
    if user.get("disabled"):
        raise HTTPException(status_code=400, detail="Inactive user")
    return user

async def authenticate_user(account: str, password: str, type: str):
    if type == "teacher":
        verify = await verify_teacher(account, password)
        if verify["flag"]:
            return {"username": verify["name"], "id": verify["id"],"role":"teacher"}
        else:
            return verify
    else:
        verify = await verify_student(account, password)
        if verify["flag"]:
            return {"username": verify["name"], "id": verify["id"],"role":"student"}
        else:
            return verify


def create_token(data: dict):
    to_encode = data.copy()
    print(to_encode)
    expires = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expires})
    jwt_encode = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return jwt_encode


async def verify_teacher(account: str, password: str):
    teacher = await Teacher.get(account=account)
    if teacher.password == password:
        return {"message": "登录成功", "id": teacher.id,"flag":True,"role":"teacher","name":teacher.name}
    return {"message": "用户名或密码错误", "flag": False}

async def verify_student(account: str, password: str):
    student = await Student.get(account=account)
    if student.pwd == password:
        return {"message": "登录成功", "id": student.id,"flag":True,"role":"student","name":student.name}
    return {"message": "用户名或密码错误", "flag": False}

async def get_user_from_db(username: str,role:str):
    if role == "teacher":
        teacher = await Teacher.get(account=username)
        return {"username": teacher.name, "id": teacher.id}
    else:
        student = await Student.get(account=username)
        return {"username": student.name, "id": student.id}
    # 模拟从数据库中查询用户信息
    return {"username": username, "disabled": False}

async def login(account: str, password: str, type: str):
    user = await authenticate_user(account, password, type)
    return create_token(user)