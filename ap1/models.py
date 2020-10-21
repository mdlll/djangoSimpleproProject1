from django.db import models


# Create your models here.
# 定义字段


class ap1Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()


class midData(models.Model):
    SEX_CHOICES = (
        (1, '男'),
        (0, '女'),
        (2, '未知')
    )

    id = models.AutoField(primary_key=True, verbose_name='主键')
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='业主姓名')
    community_id = models.IntegerField(null=True, blank=True, verbose_name='小区id')
    building_id = models.IntegerField(null=True, blank=True, verbose_name='楼栋id')
    unit_id = models.IntegerField(null=True, blank=True, verbose_name='单元id')
