from apps.core import models as core_models
from apps.users import models as users_models
from apps.seeker.models import HoSoUngTuyen


def get_data_ho_so(id):
    hoso = HoSoUngTuyen.objects.get(id=id)
    data_dict = dict()

    data_dict["fullname"] = hoso.user.fullname
    data_dict["username"] = hoso.user.username
    data_dict["birth_day"] = hoso.user.birth_day.strftime('%Y-%m-%d')
    data_dict["gioi_tinh"] = hoso.user.gender
    data_dict["dia_chi_tinh_thanh_pho"] = hoso.user.dia_chi_tinh_thanh_pho
    data_dict["dia_chi_chi_tiet"] = hoso.user.dia_chi_chi_tiet
    data_dict["sdt"] = hoso.user.sdt
    data_dict["loai_user"] = hoso.user.loai_user
    data_dict["code_hoso"] = hoso.code_hoso
    data_dict["nganh_nghe"] = hoso.nganh_nghe
    data_dict["vi_tri_mong_muon"] = hoso.vi_tri_mong_muon
    data_dict["dia_diem_lam_viec"] = hoso.dia_diem_lam_viec
    data_dict["trinh_do_hoc_van"] = hoso.trinh_do_hoc_van
    data_dict["so_nam_kinh_nghiem"] = hoso.so_nam_kinh_nghiem
    data_dict["ten_cty_tung_lam"] = hoso.ten_cty_tung_lam
    data_dict["hinh_thuc_lam_viec"] = hoso.hinh_thuc_lam_viec
    data_dict["muc_luong_toi_thieu"] = hoso.muc_luong_toi_thieu
    data_dict["ten_bang_cap"] = hoso.ten_bang_cap
    data_dict["don_vi_dao_tao"] = hoso.don_vi_dao_tao
    data_dict["chuyen_nganh"] = hoso.chuyen_nganh
    data_dict["thoi_gian_bat_dau"] = hoso.thoi_gian_bat_dau
    data_dict["thoi_gian_ket_thuc"] = hoso.thoi_gian_ket_thuc
    data_dict["loai_tot_nghiep"] = hoso.loai_tot_nghiep
    data_dict["ten_bang_cap"] = hoso.ten_bang_cap
    data_dict["ngoai_ngu"] = hoso.ngoai_ngu
    data_dict["trinh_do_ngoai_ngu"] = hoso.trinh_do_ngoai_ngu
    data_dict["ky_nang"] = hoso.ky_nang
    data_dict["hon_nhan"] = hoso.hon_nhan
    data_dict["so_thich"] = hoso.so_thich

    return data_dict

