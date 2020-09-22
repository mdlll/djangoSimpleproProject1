from django.db import models


# Create your models here.
# 定义字段


class ap1Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
