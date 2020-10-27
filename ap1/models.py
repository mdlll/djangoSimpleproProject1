from django.db import models


# Create your models here.
# 定义字段


class ap1Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()


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
    familyName = models.CharField(max_length=255, null=True, blank=True,  verbose_name='姓')
    lastName = models.CharField(max_length=255, null=True, blank=True,  verbose_name='名')
    sex = models.IntegerField(default=2, null=True, blank=True, choices=SEX_CHOICES, verbose_name='性别')
    idCard = models.CharField(max_length=255, null=True, blank=True, verbose_name='身份证')
    syncType = models.CharField(max_length=255, null=True, blank=True, verbose_name='同步类型')


class midCompany(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='主键')
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='公司名')
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name='公司地址')
    syncType = models.CharField(max_length=255, null=True, blank=True, verbose_name='同步类型')


class midCommunity(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='主键')
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='小区名')
    corpId = models.ForeignKey(midCompany, on_delete=models.CASCADE, null=True, blank=True, verbose_name='公司id')
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name='小区地址')
    nearbyLandmarks = models.CharField(max_length=255, null=True, blank=True, verbose_name='附近地标')
    longitude = models.CharField(max_length=255, null=True, blank=True,  verbose_name='经度')
    latitude = models.CharField(max_length=255, null=True, blank=True,  verbose_name='维度')
    cityCode = models.IntegerField(null=True, blank=True, verbose_name='城市代码')
    syncType = models.CharField(max_length=255, null=True, blank=True, verbose_name='同步类型')

class midBuilding(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='主键')
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='楼栋名')
    communityId = models.ForeignKey(midCommunity, on_delete=models.CASCADE, null=True, blank=True, verbose_name='小区id')
    syncType = models.CharField(max_length=255, null=True, blank=True, verbose_name='同步类型')


class midUnit(models.Model):
    Lift_CHOICES = (
        (1010, '有'),
        (2020, '无'),
    )
    id = models.AutoField(primary_key=True, verbose_name='主键')
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='单元名')
    buildingId = models.ForeignKey(midBuilding, on_delete=models.CASCADE, null=True, blank=True, verbose_name='楼栋id')
    layerCount = models.IntegerField(blank=True, null=True, verbose_name='总楼层数')
    hasLift = models.IntegerField(default=2020, null=True, blank=True, choices=Lift_CHOICES, verbose_name='是否有电梯')
    syncType = models.CharField(max_length=255, null=True, blank=True, verbose_name='同步类型')


class midRoom(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='主键')
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='房号')
    buildingId = models.ForeignKey(midBuilding, on_delete=models.CASCADE, null=True, blank=True, verbose_name='楼栋id')
    unitId = models.ForeignKey(midUnit, on_delete=models.CASCADE, null=True, blank=True, verbose_name='单元id')
    layer = models.CharField(max_length=255, null=True, blank=True, verbose_name='楼层')
    apartment = models.IntegerField(blank=True, null=True, verbose_name='户型')
    syncType = models.CharField(max_length=255, null=True, blank=True, verbose_name='同步类型')

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
    communityId = models.ForeignKey(midCompany, on_delete=models.CASCADE, null=True, blank=True, verbose_name='小区id')
    buildingId = models.ForeignKey(midBuilding, on_delete=models.CASCADE, null=True, blank=True, verbose_name='楼栋id')
    unitId = models.ForeignKey(midUnit, on_delete=models.CASCADE, null=True, blank=True, verbose_name='单元id')
    roomId = models.ForeignKey(midRoom, on_delete=models.CASCADE, null=True, blank=True, verbose_name='房屋id')
    sex = models.IntegerField(default=2, null=True, blank=True, choices=SEX_CHOICES, verbose_name='性别')
    birthday = models.CharField(max_length=255, null=True, blank=True, verbose_name='生日')
    age = models.CharField(max_length=255, null=True, blank=True, verbose_name='年龄')
    mobile = models.CharField(max_length=255, null=True, blank=True, verbose_name='联系手机')
    ownerType = models.IntegerField(default=1001, null=True, blank=True, choices=OWNER_CHOICES, verbose_name='与业主关系类型')
    status = models.IntegerField(default=0, null=True, blank=True, choices=STATUS_CHOICES, verbose_name='状态')
    syncType = models.CharField(max_length=255, null=True, blank=True, verbose_name='同步类型')