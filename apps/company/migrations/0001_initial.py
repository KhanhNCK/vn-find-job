# Generated by Django 2.2.2 on 2020-07-25 04:39

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CongTy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.CharField(default='', max_length=255, null=True)),
                ('ten_cong_ty', models.CharField(default='', max_length=255, null=True)),
                ('code_cong_ty', models.CharField(default='', max_length=255, null=True)),
                ('dia_chi', models.CharField(default='', max_length=255, null=True)),
                ('sdt_lienhe', models.CharField(default='', max_length=255, null=True)),
                ('mail_lien_he', models.CharField(default='', max_length=255, null=True)),
                ('name_lien_he', models.CharField(default='', max_length=255, null=True)),
                ('thongtin_cty', models.TextField(default='', null=True)),
            ],
            options={
                'verbose_name': 'Công ty',
                'verbose_name_plural': 'Công ty',
            },
        ),
        migrations.CreateModel(
            name='TinTuyenDung',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_tin', models.CharField(default='', max_length=255, null=True)),
                ('caption_tin_tuc', models.TextField(default='', null=True)),
                ('nganh_nghe', models.IntegerField(default=0, null=True)),
                ('muc_luong', models.IntegerField(default=0, null=True)),
                ('so_nam_kinh_nghiem', models.IntegerField(default=0, null=True)),
                ('dia_diem_lam_viec', models.IntegerField(default=0, null=True)),
                ('hinh_thuc_lam_viec', models.IntegerField(default=0, null=True)),
                ('chuc_vu', models.IntegerField(default=0, null=True)),
                ('trinh_do_hoc_van', models.IntegerField(default=0, null=True)),
                ('ngoai_ngu', models.IntegerField(default=0)),
                ('trinh_do_ngoai_ngu', models.IntegerField(default=0)),
                ('so_luong_tuyen', models.IntegerField(default=0)),
                ('mota_congviec', ckeditor_uploader.fields.RichTextUploadingField(default='')),
                ('quyenloi_congviec', ckeditor_uploader.fields.RichTextUploadingField(default='')),
                ('yeucau_congviec', ckeditor_uploader.fields.RichTextUploadingField(default='')),
                ('tag_search', models.TextField(default=0, null=True)),
                ('ngay_het_han', models.DateField(blank=True, null=True)),
                ('slug', models.CharField(default='', max_length=255, null=True)),
                ('is_send_mana', models.BooleanField(default=False)),
                ('status_tin', models.IntegerField(default=0)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('congty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.CongTy')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tin tuyển dụng',
                'verbose_name_plural': 'Tin tuyển dụng',
            },
        ),
    ]
