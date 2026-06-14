#导入tortoise

from tortoise.models import Model
from tortoise import fields


#创建班级类
class Clas(Model):
    name = fields.CharField(max_length=255, description='班级名称')


#创建老师类
class Teacher(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, description='姓名')
    tno = fields.IntField(description='账号')
    pwd = fields.CharField(max_length=255, description='密码')


#课程表
class Course(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, description='课程名')
    teacher = fields.ForeignKeyField('models.Teacher', related_name='courses', description='课程讲师')



#创建学生类
class Student(Model):
    id = fields.IntField(pk=True)
    sno = fields.IntField(description='学号')
    #description 在接口文档有个显示
    pwd = fields.CharField(max_length=255, description='密码')
    name = fields.CharField(max_length=255, description='姓名')
    # 一对多，反向查询时使用related_name
    clas = fields.ForeignKeyField('models.Clas', related_name='students')
    # 多对多
    courses = fields.ManyToManyField('models.Course', related_name='students',description='学生选课表')
