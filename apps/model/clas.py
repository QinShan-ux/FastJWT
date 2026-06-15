from tortoise import Model, fields


class Clas(Model):
    name = fields.CharField(max_length=255, description='班级名称')