from django.contrib import admin
from .models import CongTy, TinTuyenDung
# Register your models here.

class CongTyAdmin(admin.ModelAdmin):
    list_display = ('id', 'logo', 'ten_cong_ty', 'code_cong_ty', 'dia_chi', 'sdt_lienhe', 'mail_lien_he', 'name_lien_he', 'thongtin_cty')


class TinTuyenDungAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'congty', 'caption_tin_tuc','nganh_nghe','muc_luong','so_nam_kinh_nghiem','dia_diem_lam_viec','hinh_thuc_lam_viec','chuc_vu','trinh_do_hoc_van','ngoai_ngu','trinh_do_ngoai_ngu','so_luong_tuyen','mota_congviec','quyenloi_congviec','yeucau_congviec', 'tag_search')


admin.site.register(CongTy, CongTyAdmin)
admin.site.register(TinTuyenDung, TinTuyenDungAdmin)