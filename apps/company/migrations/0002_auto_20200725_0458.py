# Generated by Django 2.2.2 on 2020-07-25 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tintuyendung',
            name='ngay_het_han',
            field=models.DateField(blank=True, default='1998-09-02', null=True),
        ),
        migrations.AlterField(
            model_name='tintuyendung',
            name='ngoai_ngu',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]