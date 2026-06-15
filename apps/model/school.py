from tortoise.models import Model
from tortoise import fields

class School(Model):
    name = fields.CharField(max_length=100)
