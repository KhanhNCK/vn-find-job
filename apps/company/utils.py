from apps.core import models as core_models
from apps.users import models as users_models
from apps.company.models import TinTuyenDung


def get_data_tin_tuyendung(id):
    tin_tuyendung = TinTuyenDung.objects.get(id=id)
    data_dict = dict()

    data_dict["fullname"] = tin_tuyendung.user.fullname
    data_dict["username"] = tin_tuyendung.user.username
    data_dict["birth_day"] = tin_tuyendung.user.birth_day.strftime('%Y-%m-%d')
    data_dict["gioi_tinh"] = tin_tuyendung.user.gender
    data_dict["dia_chi_tinh_thanh_pho"] = tin_tuyendung.user.dia_chi_tinh_thanh_pho
    data_dict["dia_chi_chi_tiet"] = tin_tuyendung.user.dia_chi_chi_tiet
    data_dict["sdt"] = tin_tuyendung.user.sdt
    data_dict["loai_user"] = tin_tuyendung.user.loai_user

    data_dict["code_tin"] = tin_tuyendung.code_tin
    data_dict["caption_tin_tuc"] = tin_tuyendung.caption_tin_tuc
    data_dict["nganh_nghe"] = tin_tuyendung.nganh_nghe
    data_dict["muc_luong"] = tin_tuyendung.muc_luong
    data_dict["so_nam_kinh_nghiem"] = tin_tuyendung.so_nam_kinh_nghiem
    data_dict["dia_diem_lam_viec"] = tin_tuyendung.dia_diem_lam_viec
    data_dict["hinh_thuc_lam_viec"] = tin_tuyendung.hinh_thuc_lam_viec
    data_dict["trinh_do_hoc_van"] = tin_tuyendung.trinh_do_hoc_van
    data_dict["ngoai_ngu"] = tin_tuyendung.ngoai_ngu
    data_dict["trinh_do_ngoai_ngu"] = tin_tuyendung.trinh_do_ngoai_ngu

    data_dict["so_luong_tuyen"] = tin_tuyendung.so_luong_tuyen
    data_dict["mota_congviec"] = tin_tuyendung.mota_congviec
    data_dict["quyenloi_congviec"] = tin_tuyendung.quyenloi_congviec
    data_dict["yeucau_congviec"] = tin_tuyendung.yeucau_congviec
    data_dict["ngay_het_han"] = tin_tuyendung.ngay_het_han.strftime('%Y-%m-%d')




    return data_dict

