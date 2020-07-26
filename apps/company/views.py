from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.core.models import ThanhPho
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.views import APIView
from rest_framework import permissions,status
from apps.core.utils import validate_data, validate_response ,convert_price_to_string , convert_sex ,convert_tthn, convert_hinhthuc, convert_trinhdo, convert_hocvan, convert_ngoaingu, unique_order_id_generator
from . import models as company_models
from . import serializers as company_serializers
from django.contrib.auth import logout
from apps.core import models as core_models
from apps.seeker import models as seeker_models
from apps.users.models import User
from apps.company.tasks import gui_tin_tuyen_dung_mana

# Create your views here.

class TuyenDungView(View):
    def get(self, request):
        list_provincial=ThanhPho.objects.all().order_by("name")
        nghe_nghiep=core_models.NgheNghiep.objects.all().order_by("name_job")

        context={
            'list_provincial':list_provincial,
            'list_nghe_nghiep':nghe_nghiep
        }

        return render(request, 'company/tuyendung.html',context)


class TimHoSoAPI(APIView):
    permission_classes = (permissions.AllowAny, )
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer, )
    def post(self, request, format=None):
        valid_data = validate_data(company_serializers.TimHoSoAPISer, request.data)

        key_hoso = valid_data.get('key_hoso')
        thanh_pho = valid_data.get('thanh_pho')
        nganh_nghe = valid_data.get('nganh_nghe')
        muc_luong = valid_data.get('muc_luong')
        trinh_do = valid_data.get('trinh_do')
        kinh_nghiem = valid_data.get('kinh_nghiem')
        gioi_tinh = valid_data.get('gioi_tinh')
        ngoai_ngu = valid_data.get('ngoai_ngu')

        request.session['key_hoso_find'] = key_hoso
        request.session['thanh_pho_find'] = thanh_pho
        request.session['nganh_nghe_find'] = nganh_nghe
        request.session['muc_luong_find'] = muc_luong
        request.session['trinh_do_find'] = trinh_do
        request.session['kinh_nghiem_find'] = kinh_nghiem
        request.session['gioi_tinh_find'] = gioi_tinh
        request.session['ngoai_ngu_find'] = ngoai_ngu

        return Response(1, status=status.HTTP_200_OK)


class ListHosoView(LoginRequiredMixin,View):
    login_url = '/dang-nhap/'
    def get(self, request):
        nghe_nghiep=core_models.NgheNghiep.objects.all().order_by("name_job")
        thanh_pho=core_models.ThanhPho.objects.all().order_by("name")
        user=User.objects.get(id=request.user.id)

        if user.loai_user == 1:
            logout(request)
            context={'list_nghe_nghiep':nghe_nghiep,'list_thanh_pho':thanh_pho,'user':user}
            return render(request, 'company/yeu_cau_login.html',context)
        else:
            key_hoso=request.session.get('key_hoso_find')
            thanh_pho=request.session.get('thanh_pho_find')
            nganh_nghe=request.session.get('nganh_nghe_find')
            muc_luong=request.session.get('muc_luong_find')
            trinh_do=request.session.get('trinh_do_find')
            kinh_nghiem=request.session.get('kinh_nghiem_find')
            gioi_tinh=request.session.get('gioi_tinh_find')
            ngoai_ngu=request.session.get('ngoai_ngu_find')

            if nganh_nghe == 0:
                if thanh_pho == 0:
                    if trinh_do == 0:
                        if kinh_nghiem == 0:
                            if gioi_tinh == 0:
                                if ngoai_ngu == "":
                                    hoso=seeker_models.HoSoUngTuyen.objects.filter(key_word__icontains=key_hoso, status_hoso=1)
                                else:
                                    hoso=seeker_models.HoSoUngTuyen.objects.filter(ngoai_ngu=ngoai_ngu, status_hoso=1)
                            else:
                                hoso=seeker_models.HoSoUngTuyen.objects.filter(user__gender=gioi_tinh, status_hoso=1)
                        else:
                            hoso=seeker_models.HoSoUngTuyen.objects.filter(so_nam_kinh_nghiem=kinh_nghiem, status_hoso=1)
                    else:
                        hoso=seeker_models.HoSoUngTuyen.objects.filter(trinh_do_hoc_van=trinh_do, status_hoso=1)
                else:
                    hoso=seeker_models.HoSoUngTuyen.objects.filter(dia_diem_lam_viec=thanh_pho, status_hoso=1)
            else:
                hoso=seeker_models.HoSoUngTuyen.objects.filter(nganh_nghe=nganh_nghe, status_hoso=1)

            list_it=[]
            for it in hoso:
                sub_item = {}
                dia_diem=core_models.ThanhPho.objects.get(code=it.dia_diem_lam_viec)
                nghe_nghiep=core_models.NgheNghiep.objects.get(code_job=it.nganh_nghe)

                sub_item['nghe_nghiep'] = nghe_nghiep.name_job
                sub_item['vi_tri_mong_muon'] = it.vi_tri_mong_muon
                sub_item['dia_diem'] = dia_diem.name
                sub_item['muc_luong'] = it.muc_luong_toi_thieu
                sub_item['hinh_thuc_lv'] = it.hinh_thuc_lam_viec
                sub_item['fullname'] = it.user.fullname
                sub_item['slug'] = it.slug

                list_it.append(sub_item)

            context={
                'list_nghe_nghiep':nghe_nghiep,
                'list_thanh_pho':thanh_pho,
                'hoso_ungvien':list_it,
                'user':user,

            }
            return render(request, 'company/ho_so_uv.html',context)


class DetailHoSoView(LoginRequiredMixin,View):
    login_url = '/dang-nhap/'

    def get(self, request, slug):
        user=User.objects.get(id=request.user.id)
        thanh_pho=core_models.ThanhPho.objects.all().order_by("name")
        nghe_nghiep=core_models.NgheNghiep.objects.all().order_by("name_job")
        if user.loai_user == 1:
            logout(request)
            context={'list_nghe_nghiep':nghe_nghiep,'list_thanh_pho':thanh_pho,'user':user}
            return render(request, 'job_detail/yeu_cau_login.html',context)
        else:
            hoso=seeker_models.HoSoUngTuyen.objects.get(slug=slug)
            list_it=[]
            sub_item = {}
            dia_diem=core_models.ThanhPho.objects.get(code=hoso.dia_diem_lam_viec)
            nghe_nghiep=core_models.NgheNghiep.objects.get(code_job=hoso.nganh_nghe)
            sub_item['nghe_nghiep'] = nghe_nghiep.name_job
            sub_item['vi_tri_mong_muon'] = hoso.vi_tri_mong_muon
            sub_item['dia_diem'] = dia_diem.name
            sub_item['trinh_do_hoc_van'] = convert_hocvan(hoso.trinh_do_hoc_van)
            sub_item['so_nam_kinh_nghiem'] = hoso.so_nam_kinh_nghiem
            sub_item['ten_cty_tung_lam'] = hoso.ten_cty_tung_lam
            sub_item['hinh_thuc_lam_viec'] = convert_hinhthuc(hoso.hinh_thuc_lam_viec)
            sub_item['muc_luong'] = convert_price_to_string(int(hoso.muc_luong_toi_thieu))
            sub_item['ngoai_ngu'] = convert_ngoaingu(hoso.ngoai_ngu)
            sub_item['trinh_do_ngoai_ngu'] = convert_trinhdo(hoso.trinh_do_ngoai_ngu)
            sub_item['ky_nang'] = hoso.ky_nang
            sub_item['so_thich'] = hoso.so_thich
            sub_item['code_hoso'] = hoso.code_hoso
            sub_item['create_at'] = hoso.create_at

            sub_item['fullname'] = hoso.user.fullname
            sub_item['sdt'] = hoso.user.sdt
            sub_item['username'] = hoso.user.username
            sub_item['dia_chi_chi_tiet'] = hoso.user.dia_chi_chi_tiet
            sub_item['gender'] = convert_sex(hoso.user.gender)
            sub_item['birth_day'] = hoso.user.birth_day

            list_it.append(sub_item)

            context={
                'list_provincial':thanh_pho,
                'list_nghe_nghiep':nghe_nghiep,
                'hoso':list_it
            }

            return render(request, 'company/detail_hoso.html',context)


class TaoTinTuyendungView(LoginRequiredMixin,View):
    login_url = '/dang-nhap/'
    def get(self, request):
        nghe_nghiep=core_models.NgheNghiep.objects.all().order_by("name_job")
        thanh_pho=core_models.ThanhPho.objects.all().order_by("name")
        user=User.objects.get(id=request.user.id)
        if user.loai_user == 1:
            logout(request)
            context={'list_nghe_nghiep':nghe_nghiep,'list_thanh_pho':thanh_pho,'user':user}
            return render(request, 'job_detail/yeu_cau_login.html',context)
        else:
            if seeker_models.HoSoUngTuyen.objects.filter(user=request.user).exists():
                tin_tuyen_dung=seeker_models.HoSoUngTuyen.objects.get(user=user)
                context={
                    'list_nghe_nghiep':nghe_nghiep,
                    'list_thanh_pho':thanh_pho,
                    'tin_td':tin_tuyen_dung,
                    'user':user,
                    'gt':convert_sex(user.gender), 
                    'hoc_van':convert_hocvan(tin_tuyen_dung.trinh_do_hoc_van),
                    'hinh_thuc':convert_hinhthuc(tin_tuyen_dung.hinh_thuc_lam_viec),
                    'td_nn':convert_trinhdo(tin_tuyen_dung.trinh_do_ngoai_ngu),
                    'nn':convert_ngoaingu(tin_tuyen_dung.ngoai_ngu)
                }
            else:
                context={
                    'list_nghe_nghiep':nghe_nghiep,
                    'list_thanh_pho':thanh_pho,
                    'user':user,
                }
            return render(request, 'company/tao_tintd.html',context)


class SubmitInfoCtyAPI(APIView):
    permission_classes = (permissions.AllowAny, )
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer, )
    def post(self, request, format=None):
        valid_data = validate_data(company_serializers.SubmitInfoCtyAPISer, request.data)

        ten_cong_ty = valid_data.get('ten_cong_ty')
        dien_thoai_cty = valid_data.get('dien_thoai_cty')
        ng_cty = valid_data.get('ng_cty')
        dia_chi_cty = valid_data.get('dia_chi_cty')
        email_cty = valid_data.get('email_cty')
        info_cty = valid_data.get('info_cty')
        
        if ten_cong_ty == "" or dien_thoai_cty == "" or ng_cty == "" or dia_chi_cty == "" or email_cty == "" or info_cty == "":
            return Response(data={"err":2}, status=status.HTTP_200_OK)
        else:
            request.session['ten_cong_ty']=ten_cong_ty
            request.session['dien_thoai_cty']=dien_thoai_cty
            request.session['ng_cty']=ng_cty
            request.session['dia_chi_cty']=dia_chi_cty
            request.session['email_cty']=email_cty
            request.session['info_cty']=info_cty

            return Response(data={"err":1}, status=status.HTTP_200_OK)


class SubmitInfoNormalAPI(APIView):
    permission_classes = (permissions.AllowAny, )
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer, )
    def post(self, request, format=None):
        valid_data = validate_data(company_serializers.SubmitInfoNormalAPISer, request.data)

        title_tin = valid_data.get('title_tin')
        nganh_nghe = valid_data.get('nganh_nghe')
        thanh_pho_lv = valid_data.get('thanh_pho_lv')
        trinh_do = valid_data.get('trinh_do')
        nam_kn = valid_data.get('nam_kn')
        hinhthuc_lv = valid_data.get('hinhthuc_lv')
        luong_sal = valid_data.get('luong_sal')
        so_luong_tuyen = valid_data.get('so_luong_tuyen')
        ngay_het_han = valid_data.get('ngay_het_han')


        if title_tin == "" or nganh_nghe == 0 or thanh_pho_lv == 0 or trinh_do == 0 or nam_kn == 0 or hinhthuc_lv == 0 or luong_sal == "" or so_luong_tuyen == 0 or ngay_het_han == "":
            return Response(data={"err":2}, status=status.HTTP_200_OK)
        else:
            request.session['title_tin']=title_tin
            request.session['nganh_nghe_tin']=nganh_nghe
            request.session['thanh_pho_lv_tin']=thanh_pho_lv
            request.session['trinh_do_tin']=trinh_do
            request.session['nam_kn_tin']=nam_kn
            request.session['hinhthuc_lv_tin']=hinhthuc_lv
            request.session['luong_sal_tin']=luong_sal
            request.session['so_luong_tuyen_tin']=so_luong_tuyen
            request.session['ngay_het_han_tin']=ngay_het_han
            
            data={
                "err":1,
                'hoc_van':convert_hocvan(trinh_do),
                'hinh_thuc':convert_hinhthuc(hinhthuc_lv),
            }
            return Response(data=data, status=status.HTTP_200_OK)


class SubmitInfoNgoaiNguAPI(APIView):
    permission_classes = (permissions.AllowAny, )
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer, )
    def post(self, request, format=None):
        valid_data = validate_data(company_serializers.SubmitInfoNgoaiNguAPISer, request.data)
        ngoai_ngu = valid_data.get('ngoai_ngu')
        trinh_do_nn = valid_data.get('trinh_do_nn')
        mota_cviec = valid_data.get('mota_cviec')
        ql_cviec = valid_data.get('ql_cviec')
        yc_cviec = valid_data.get('yc_cviec')

        if ngoai_ngu == "" or trinh_do_nn == 0 or mota_cviec == "" or ql_cviec == "" or yc_cviec == "":
            return Response(data={"err":2}, status=status.HTTP_200_OK)
        else:
            request.session['ngoai_ngu_tin']=ngoai_ngu
            request.session['trinh_do_nn_tin']=trinh_do_nn
            request.session['mota_cviec_tin']=mota_cviec
            request.session['ql_cviec_tin']=ql_cviec
            request.session['yc_cviec_tin']=yc_cviec

            return Response(data={"err":1,'tdnn':convert_trinhdo(trinh_do_nn),'nn_lv':convert_ngoaingu(ngoai_ngu)}, status=status.HTTP_200_OK)


class SubmitDuyetTinTuyenDungAPI(APIView):
    permission_classes = (permissions.AllowAny, )
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer, )
    def post(self, request, format=None):
        valid_data = validate_data(company_serializers.SubmitDuyetTinTuyenDungAPISer, request.data)
        check_val1 = valid_data.get('check_val1')
        check_val2 = valid_data.get('check_val2')
        check_val3 = valid_data.get('check_val3')

        if check_val1 == 1 and check_val2 == 1 and check_val3 == 1:
            user = User.objects.get(id=request.user.id)
            code_tin = unique_order_id_generator(request.user.username,2)
            code_cong_ty=unique_order_id_generator(request.user.username,2)

            ten_cong_ty=request.session['ten_cong_ty']
            dien_thoai_cty=request.session['dien_thoai_cty']
            ng_cty=request.session['ng_cty']
            dia_chi_cty=request.session['dia_chi_cty']
            email_cty=request.session['email_cty']
            info_cty=request.session['info_cty']

            title_tin=request.session['title_tin']
            nganh_nghe=request.session['nganh_nghe_tin']
            thanh_pho_lv=request.session['thanh_pho_lv_tin']
            trinh_do=request.session['trinh_do_tin']
            nam_kn=request.session['nam_kn_tin']
            hinhthuc_lv=request.session['hinhthuc_lv_tin']
            luong_sal=request.session['luong_sal_tin']
            so_luong_tuyen=request.session['so_luong_tuyen_tin']
            ngay_het_han=request.session['ngay_het_han_tin']

            ngoai_ngu=request.session['ngoai_ngu_tin']
            trinh_do_nn=request.session['trinh_do_nn_tin']
            mota_cviec=request.session['mota_cviec_tin']
            ql_cviec=request.session['ql_cviec_tin']
            yc_cviec=request.session['yc_cviec_tin']

            cong_ty=company_models.CongTy.objects.create(ten_cong_ty=ten_cong_ty,code_cong_ty=code_cong_ty,dia_chi=dia_chi_cty,
                                                        sdt_lienhe=dien_thoai_cty,mail_lien_he=email_cty,name_lien_he=ng_cty,thongtin_cty=info_cty)
            tin_tuyen_dung=company_models.TinTuyenDung.objects.create(user=user,congty=cong_ty,caption_tin_tuc=title_tin,nganh_nghe=nganh_nghe,muc_luong=luong_sal,
                                                                so_nam_kinh_nghiem=nam_kn,dia_diem_lam_viec=thanh_pho_lv,hinh_thuc_lam_viec=hinhthuc_lv,
                                                                trinh_do_hoc_van=trinh_do,ngoai_ngu=ngoai_ngu,trinh_do_ngoai_ngu=trinh_do_nn,so_luong_tuyen=so_luong_tuyen,
                                                                mota_congviec=mota_cviec,quyenloi_congviec=ql_cviec,yeucau_congviec=yc_cviec,ngay_het_han=ngay_het_han)
            gui_tin_tuyen_dung_mana.delay(tin_tuyen_dung.id)
            return Response(1, status=status.HTTP_200_OK)
        else:
            return Response(1, status=status.HTTP_400_BAD_REQUEST)


class FeedbackTinTuyenDungMana(APIView):
    permission_classes = (permissions.AllowAny, )
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer, )
    def post(self, request, format=None):
        valid_data = validate_data(company_serializers.FeedbackTinTuyenDungManaSer, request.data)
        ten_day_du = valid_data.get('ten_day_du')

  
        return Response(1, status=status.HTTP_200_OK)