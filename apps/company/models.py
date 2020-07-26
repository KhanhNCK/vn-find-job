from django.db import models
from apps.users.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from apps.core.models import NgheNghiep,ThanhPho

# Create your models here.

class CongTy(models.Model):
    logo =  models.CharField(null = True, max_length=255, default="")
    ten_cong_ty = models.CharField(default="", max_length=255, null=True)
    code_cong_ty = models.CharField(default="", null=True, max_length=255,)
    dia_chi = models.CharField(max_length=255, default="", null=True)
    sdt_lienhe = models.CharField(max_length=255, default="", null=True)
    mail_lien_he = models.CharField(max_length=255, default="", null=True)
    name_lien_he = models.CharField(max_length=255, default="", null=True)
    thongtin_cty=models.TextField(default="", null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Công ty'
        verbose_name_plural = 'Công ty'


class TinTuyenDung(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    congty=models.ForeignKey(CongTy, on_delete=models.CASCADE)
    code_tin = models.CharField(max_length=255, default='', null=True)
    caption_tin_tuc = models.TextField(default='', null=True)
    nganh_nghe = models.IntegerField(default=0, null=True)
    muc_luong = models.IntegerField(default=0, null=True)
    so_nam_kinh_nghiem = models.IntegerField(default=0, null=True)
    dia_diem_lam_viec = models.IntegerField(default=0, null=True)
    hinh_thuc_lam_viec = models.IntegerField(default=0, null=True)
    chuc_vu = models.IntegerField(default=0, null=True)
    trinh_do_hoc_van = models.IntegerField(default=0, null=True)
    ngoai_ngu = models.CharField(max_length=255, default='', null=True)
    trinh_do_ngoai_ngu = models.IntegerField(default=0)
    so_luong_tuyen = models.IntegerField(default=0)
    mota_congviec = RichTextUploadingField(default='')
    quyenloi_congviec = RichTextUploadingField(default='')
    yeucau_congviec = RichTextUploadingField(default='')
    tag_search = models.TextField(default=0, null=True)
    ngay_het_han = models.DateField(blank=True, null=True,default='1998-09-02')
    slug = models.CharField(max_length=255, default="", null=True)
    is_send_mana=models.BooleanField(default=False)
    status_tin=models.IntegerField(default=0)   #0 chua duyet, 1 da duyet, 2 huy bo
    create_at = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Tin tuyển dụng'
        verbose_name_plural = 'Tin tuyển dụng'