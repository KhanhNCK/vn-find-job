from rest_framework import serializers


class TimHoSoAPISer(serializers.Serializer):
    key_hoso = serializers.CharField(allow_blank=True)
    thanh_pho = serializers.IntegerField()
    nganh_nghe = serializers.IntegerField()
    muc_luong = serializers.IntegerField()
    trinh_do = serializers.IntegerField()
    kinh_nghiem = serializers.IntegerField()
    gioi_tinh = serializers.IntegerField()
    ngoai_ngu = serializers.CharField(allow_blank=True)


class SubmitInfoCtyAPISer(serializers.Serializer):
    ten_cong_ty = serializers.CharField()
    dien_thoai_cty = serializers.CharField()
    ng_cty = serializers.CharField()
    dia_chi_cty = serializers.CharField()
    email_cty = serializers.CharField()
    info_cty = serializers.CharField()


class SubmitInfoNormalAPISer(serializers.Serializer):
    title_tin = serializers.CharField()
    nganh_nghe = serializers.IntegerField()
    thanh_pho_lv = serializers.IntegerField()
    trinh_do = serializers.IntegerField()
    nam_kn = serializers.IntegerField()
    hinhthuc_lv = serializers.IntegerField()
    luong_sal = serializers.CharField()
    so_luong_tuyen = serializers.IntegerField()
    ngay_het_han = serializers.CharField()


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
    mota_cviec = serializers.CharField()
    ql_cviec = serializers.CharField()
    yc_cviec = serializers.CharField()


class SubmitDuyetTinTuyenDungAPISer(serializers.Serializer):
    check_val1 = serializers.IntegerField()
    check_val2 = serializers.IntegerField()
    check_val3 = serializers.IntegerField()


class FeedbackTinTuyenDungManaSer(serializers.Serializer):
    check_val1 = serializers.IntegerField()
    check_val2 = serializers.IntegerField()
    check_val3 = serializers.IntegerField()

