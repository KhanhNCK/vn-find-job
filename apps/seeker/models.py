from django.db import models
from apps.users.models import User
from apps.core.models import NgheNghiep,ThanhPho

# Create your models here.
'''
trinh_do_hoc_van:
    1: chung chi nghe
    2: trung cap
    3: cao dang
    4: dai hoc
    5: tren dai hoc

hinh_thuc_lam_viec:
    1: hop dong
    2: ban thoi gian
    3: toan thoi gian tam thoi
    4: toan thoi gian co dinh
loai_tot_nghiep,trinh_do_ngoai_ngu:
    1: Xuat sac
    2: gioi
    3: kha
    4: trung binh
hon_nhan:
    1: da ket hon
    2: doc than
    3: khac
ky_nang:
    1: lanh dao
    2: tu hoc
'''

class HoSoUngTuyen(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code_hoso = models.CharField(max_length=255, default="", null=True)
    nganh_nghe = models.IntegerField(default=0, null=True)
    vi_tri_mong_muon = models.CharField(max_length=255, default="", null=True)
    dia_diem_lam_viec = models.IntegerField(default=0, null=True)
    trinh_do_hoc_van = models.IntegerField(default=0, null=True)
    so_nam_kinh_nghiem = models.IntegerField(default=0, null=True)
    ten_cty_tung_lam = models.CharField(max_length=255, default="", null=True)
    hinh_thuc_lam_viec = models.IntegerField(default=0, null=True)
    muc_luong_toi_thieu = models.CharField(max_length=255, default="", null=True)
    ten_bang_cap = models.CharField(max_length=255, default="", null=True)
    don_vi_dao_tao = models.CharField(max_length=255, default="", null=True)
    chuyen_nganh = models.CharField(max_length=255, default="", null=True)
    thoi_gian_bat_dau = models.CharField(max_length=255, default="", null=True)
    thoi_gian_ket_thuc = models.CharField(max_length=255, default="", null=True)
    loai_tot_nghiep = models.IntegerField(default=0, null=True)
    ngoai_ngu = models.CharField(max_length=255, default="", null=True)
    trinh_do_ngoai_ngu = models.IntegerField(default=0)
    ky_nang =  models.TextField(default="", null=True)
    hon_nhan = models.IntegerField(default=0)
    so_thich = models.TextField(default="", null=True)
    slug = models.CharField(max_length=255, default="", null=True)
    key_word = models.TextField(default="", null=True)
    is_send_mana=models.BooleanField(default=False)
    status_hoso=models.IntegerField(default=0)   #0 chua duyet, 1 da duyet, 2 huy bo
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Hồ sơ ứng tuyển'
        verbose_name_plural = 'Hồ sơ ứng tuyển'