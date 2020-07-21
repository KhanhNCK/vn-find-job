from django.db import models
from apps.users.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from apps.core.models import NgheNghiep,ThanhPho

# Create your models here.

class CongTy(models.Model):
    logo =  models.CharField(null = True, max_length=255, default=None)
    ten_cong_ty = models.CharField(default=None, max_length=255, null=True)
    code_cong_ty = models.IntegerField(default=0, null=True)
    dia_chi = models.CharField(max_length=255, default=None, null=True)
    sdt_lienhe = models.CharField(max_length=255, default=None, null=True)
    mail_lien_he = models.CharField(max_length=255, default=None, null=True)
    name_lien_he = models.CharField(max_length=255, default=None, null=True)
    thongtin_cty=models.TextField(default=None, null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Công ty'
        verbose_name_plural = 'Công ty'


class TinTuyenDung(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    congty=models.ForeignKey(CongTy, on_delete=models.CASCADE)
    caption_tin_tuc = models.CharField(max_length=255, default=None, null=True)
    nganh_nghe = models.ForeignKey(NgheNghiep, on_delete=models.CASCADE)
    muc_luong = models.IntegerField(default=0, null=True)
    so_nam_kinh_nghiem = models.IntegerField(default=0, null=True)
    dia_diem_lam_viec = models.ForeignKey(ThanhPho, on_delete=models.CASCADE)
    hinh_thuc_lam_viec = models.IntegerField(default=0, null=True)
    chuc_vu = models.IntegerField(default=0, null=True)
    trinh_do_hoc_van = models.IntegerField(default=0, null=True)
    ngoai_ngu = models.IntegerField(default=0)
    trinh_do_ngoai_ngu = models.IntegerField(default=0)
    so_luong_tuyen = models.IntegerField(default=0)
    mota_congviec = RichTextUploadingField(default='')
    quyenloi_congviec = RichTextUploadingField(default='')
    yeucau_congviec = RichTextUploadingField(default='')
    tag_search = models.TextField()
    ngay_het_han = models.DateField()
    slug = models.CharField(max_length=255, default=None, null=True)
    create_at = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Tin tuyển dụng'
        verbose_name_plural = 'Tin tuyển dụng'