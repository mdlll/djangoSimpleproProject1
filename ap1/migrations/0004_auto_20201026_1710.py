# Generated by Django 3.1.1 on 2020-10-26 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ap1', '0003_auto_20201026_1520'),
    ]

    operations = [
        migrations.RenameField(
            model_name='midadmin',
            old_name='family_name',
            new_name='familyName',
        ),
        migrations.RenameField(
            model_name='midadmin',
            old_name='id_card',
            new_name='idCard',
        ),
        migrations.RenameField(
            model_name='midadmin',
            old_name='last_name',
            new_name='lastName',
        ),
        migrations.RenameField(
            model_name='midadmin',
            old_name='sync_type',
            new_name='syncType',
        ),
        migrations.RenameField(
            model_name='midbuilding',
            old_name='community_id',
            new_name='communityId',
        ),
        migrations.RenameField(
            model_name='midbuilding',
            old_name='sync_type',
            new_name='syncType',
        ),
        migrations.RenameField(
            model_name='midcommunity',
            old_name='city_code',
            new_name='cityCode',
        ),
        migrations.RenameField(
            model_name='midcommunity',
            old_name='corp_id',
            new_name='corpId',
        ),
        migrations.RenameField(
            model_name='midcommunity',
            old_name='username',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='midcommunity',
            old_name='nearly_by_landmarks',
            new_name='nearbyLandmarks',
        ),
        migrations.RenameField(
            model_name='midcommunity',
            old_name='sync_type',
            new_name='syncType',
        ),
        migrations.RenameField(
            model_name='midcompany',
            old_name='sync_type',
            new_name='syncType',
        ),
        migrations.RenameField(
            model_name='midinhabitant',
            old_name='building_id',
            new_name='buildingId',
        ),
        migrations.RenameField(
            model_name='midinhabitant',
            old_name='community_id',
            new_name='communityId',
        ),
        migrations.RenameField(
            model_name='midinhabitant',
            old_name='room_id',
            new_name='roomId',
        ),
        migrations.RenameField(
            model_name='midinhabitant',
            old_name='sync_type',
            new_name='syncType',
        ),
        migrations.RenameField(
            model_name='midinhabitant',
            old_name='unit_id',
            new_name='unitId',
        ),
        migrations.RenameField(
            model_name='midroom',
            old_name='building_id',
            new_name='buildingId',
        ),
        migrations.RenameField(
            model_name='midroom',
            old_name='sync_type',
            new_name='syncType',
        ),
        migrations.RenameField(
            model_name='midroom',
            old_name='unit_id',
            new_name='unitId',
        ),
        migrations.RenameField(
            model_name='midunit',
            old_name='building_id',
            new_name='buildingId',
        ),
        migrations.RenameField(
            model_name='midunit',
            old_name='layer_count',
            new_name='layerCount',
        ),
        migrations.RenameField(
            model_name='midunit',
            old_name='sync_type',
            new_name='syncType',
        ),
        migrations.RemoveField(
            model_name='midunit',
            name='lift',
        ),
        migrations.AddField(
            model_name='midunit',
            name='hasLift',
            field=models.IntegerField(blank=True, choices=[(1010, '有'), (2020, '无')], default=2020, null=True, verbose_name='是否有电梯'),
        ),
        migrations.AlterField(
            model_name='midinhabitant',
            name='ownerType',
            field=models.IntegerField(blank=True, choices=[(1001, '本人'), (1002, '家庭成员')], default=1001, null=True, verbose_name='与业主关系类型'),
        ),
    ]
