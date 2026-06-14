from tortoise import fields, Model


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