# Generated by Django 2.2.2 on 2020-07-22 04:18

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200, null=True)),
                ('link_video', models.CharField(default=None, max_length=255, null=True)),
                ('sub_title', models.CharField(max_length=200)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(default='')),
                ('images_gioi_thieu', models.TextField(default=None, null=True)),
                ('sub_content', ckeditor_uploader.fields.RichTextUploadingField(default='')),
                ('seo_key_word', models.CharField(default=None, max_length=200, null=True)),
                ('status', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Tin tức',
                'verbose_name_plural': 'Tin tức',
            },
        ),
    ]
