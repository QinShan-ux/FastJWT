from tortoise import fields
from tortoise.models import Model

class Teacher(Model):
    name = fields.CharField(max_length=100)
    age = fields.IntField()
    address = fields.CharField(max_length=100)
    account = fields.CharField(max_length=100)
    password = fields.CharField(max_length=100)
    id = fields.IntField(pk=True,auto=True,generated=True)


