from datetime import timedelta, datetime, timezone

import jwt
from pwdlib import PasswordHash

from apps.model.student import Student
from apps.model.teacher import Teacher
password_hash = PasswordHash.recommended()
DUMMY_HASH = password_hash.hash("dummypassword")
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

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

async def login(account: str, password: str, type: str):
    user = await authenticate_user(account, password, type)
    return create_token(user)