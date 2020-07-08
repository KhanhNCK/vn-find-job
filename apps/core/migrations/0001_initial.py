# Generated by Django 2.2.2 on 2020-07-02 18:29

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NgheNghiep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_job', models.IntegerField(default=0, null=True)),
                ('code_job', models.CharField(default=None, max_length=255, null=True)),
                ('job_info', ckeditor_uploader.fields.RichTextUploadingField(default='')),
            ],
            options={
                'verbose_name': 'Nghề nghiệp',
                'verbose_name_plural': 'Nghề nghiệp',
            },
        ),
        migrations.CreateModel(
            name='ThanhPho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.IntegerField(default=0)),
                ('group', models.IntegerField(default=0)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
            ],
            options={
                'verbose_name': 'Tỉnh/thành phố ',
                'verbose_name_plural': 'Tỉnh/thành phố',
            },
        ),
    ]
