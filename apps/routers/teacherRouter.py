from typing import Annotated

from fastapi import APIRouter, Depends, Path
from pydantic import BaseModel
from apps.core.security import get_current_user, api_key_header
from apps.model.teacher import Teacher

class TeacherCreate(BaseModel):
    name: str
    age: int
    address: str
    account: str
    password: str

router = APIRouter(
    prefix="/teacher",
    tags=["teacher"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(get_current_user)]
)

@router.get("/test")
async def test():
    return {"message": "Hello World"}
@router.get("/{teacher_id}",summary="获取教师信息",description="获取教师信息")
async def get_teacher(
    teacher_id: Annotated[int, Path(description="教师ID")]           # ✅ 路径参数
):
    res = await Teacher.get(id=teacher_id)
    return res


@router.post("/add",summary="添加教师信息",description="添加教师信息")
async def add_teacher(teacher: TeacherCreate):
    res = await Teacher.create(
        name=teacher.name,
        age=teacher.age,
        address=teacher.address,
        account=teacher.account,
        password=teacher.password,
    )
    return res
