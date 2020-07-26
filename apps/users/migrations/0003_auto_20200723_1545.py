# Generated by Django 2.2.2 on 2020-07-23 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_sdt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dia_chi_chi_tiet',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='dia_chi_quan_huyen',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='dia_chi_tinh_thanh_pho',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='fullname',
            field=models.CharField(default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='images_user',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='sdt',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]
