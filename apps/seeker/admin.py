from django.contrib import admin
from .models import HoSoUngTuyen
# Register your models here.

class HoSoUngTuyenAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'nganh_nghe','vi_tri_mong_muon','dia_diem_lam_viec','trinh_do_hoc_van','so_nam_kinh_nghiem','ten_cty_tung_lam','hinh_thuc_lam_viec','muc_luong_toi_thieu','ten_bang_cap','don_vi_dao_tao','chuyen_nganh','thoi_gian_bat_dau','thoi_gian_ket_thuc','loai_tot_nghiep','ngoai_ngu','trinh_do_ngoai_ngu','ky_nang','hon_nhan','so_thich')


admin.site.register(HoSoUngTuyen, HoSoUngTuyenAdmin)