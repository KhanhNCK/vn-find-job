from rest_framework import serializers


class SubmitInfoAccAPISer(serializers.Serializer):
    ten_day_du = serializers.CharField()
    dien_thoai_lien_he = serializers.CharField()
    ngay_sinh = serializers.CharField()
    dia_chi_lien_he = serializers.CharField()
    thanh_pho_song = serializers.IntegerField()
    gioi_tinh = serializers.IntegerField()
    tinh_trang_hn = serializers.IntegerField()


class SubmitInfoNormalAPISer(serializers.Serializer):
    vi_tri = serializers.CharField()
    nganh_nghe = serializers.IntegerField()
    thanh_pho_lv = serializers.IntegerField()
    trinh_do = serializers.IntegerField()
    nam_kn = serializers.IntegerField()
    hinhthuc_lv = serializers.IntegerField()
    luong_sal = serializers.CharField()


class SubmitInfoExpAPISer(serializers.Serializer):
    cty_lv = serializers.CharField()
    bang_cap = serializers.CharField()
    dao_tao = serializers.CharField()
    chuyen_nganh = serializers.CharField()
    bat_dau = serializers.CharField()
    ket_thuc = serializers.CharField()
    loai_tot_nghiep = serializers.IntegerField()


class SubmitInfoNgoaiNguAPISer(serializers.Serializer):
    ngoai_ngu = serializers.CharField()
    trinh_do_nn = serializers.IntegerField()
    ky_nang = serializers.CharField()
    so_thich = serializers.CharField()


class SubmitDuyetHoSoAPISer(serializers.Serializer):
    mana = serializers.IntegerField()

class FeedbackHoSoManaSer(serializers.Serializer):
    mana = serializers.IntegerField()
