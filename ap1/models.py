from django.db import models


# Create your models here.
# 定义字段


class ap1Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()


class midInhabitant(models.Model):
    SEX_CHOICES = (
        (1, '男'),
        (0, '女'),
        (2, '未知')
    )
    OWNER_CHOICES = {
        (1001, '本人'),
        (1002, '家庭成员')
    }
    STATUS_CHOICES = {
        (0, '无效'),
        (1, '有效')
    }

    id = models.AutoField(primary_key=True, verbose_name='主键')
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='业主姓名')
    community_id = models.IntegerField(null=True, blank=True, verbose_name='小区id')
    building_id = models.IntegerField(null=True, blank=True, verbose_name='楼栋id')
    unit_id = models.IntegerField(null=True, blank=True, verbose_name='单元id')
    room_id = models.IntegerField(null=True, blank=True, verbose_name='房屋id')
    sex = models.CharField(max_length=255, null=True, blank=True, choices=SEX_CHOICES, verbose_name='性别')
    birthday = models.CharField(max_length=255, null=True, blank=True, verbose_name='生日')
    age = models.CharField(max_length=255, null=True, blank=True, verbose_name='年龄')
    mobile = models.CharField(max_length=255, null=True, blank=True, verbose_name='联系手机')
    ownerType = models.CharField(max_length=255, null=True, blank=True, choices=OWNER_CHOICES, verbose_name='与业主关系类型')
    status = models.CharField(max_length=255, null=True, blank=True, choices=STATUS_CHOICES, verbose_name='状态')
    sync_type = models.CharField(max_length=255, null=True, blank=True, verbose_name='同步类型')


class midAdmin(models.Model):
    SEX_CHOICES = (
        (1, '男'),
        (0, '女'),
        (2, '未知')
    )
    id = models.AutoField(primary_key=True, verbose_name='主键')
    username = models.CharField(max_length=255, blank=True, null=True, verbose_name='用户名')
    pwd = models.CharField(max_length=255, null=True, blank=True, verbose_name='密码')
    email = models.CharField(max_length=255, null=True, blank=True, verbose_name='电子邮箱')
    mobile = models.CharField(max_length=255, null=True, blank=True, verbose_name='手机号')
    family_name = models.CharField(max_length=255, null=True, blank=True,  verbose_name='姓')
    last_name = models.CharField(max_length=255, null=True, blank=True,  verbose_name='名')
    sex = models.CharField(max_length=255, null=True, blank=True, choices=SEX_CHOICES, verbose_name='性别')
    id_card = models.CharField(max_length=255, null=True, blank=True, verbose_name='身份证')
    sync_type = models.CharField(max_length=255, null=True, blank=True, verbose_name='同步类型')
