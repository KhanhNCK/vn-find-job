from django.shortcuts import render
from django.views import View
from apps.core import models as core_models
from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.views import APIView
from rest_framework import permissions,status
from apps.core.utils import validate_data, validate_response ,convert_price_to_string , convert_sex ,convert_tthn, convert_hinhthuc, convert_trinhdo, convert_hocvan, convert_ngoaingu, unique_order_id_generator
from . import models as seeker_models
from . import serializers as seeker_serializers
from apps.seeker.tasks import gui_hoso_mana
from apps.users.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from apps.company.models import TinTuyenDung
from django.db.models import Q
from apps.company import models as company_models
from django.core.paginator import Paginator

# Create your views here.


class ListJobViewFull(View):
    def get(self, request):
        nghe_nghiep=core_models.NgheNghiep.objects.all().order_by("name_job")
        thanh_pho=core_models.ThanhPho.objects.all().order_by("name")
        list_full=[]
        if TinTuyenDung.objects.filter(Q(status_tin=1,hinh_thuc_lam_viec=1) | Q(status_tin=1,hinh_thuc_lam_viec=2)).order_by("create_at").exists():
            job_full=TinTuyenDung.objects.filter(Q(status_tin=1,hinh_thuc_lam_viec=1) | Q(status_tin=1,hinh_thuc_lam_viec=2)).order_by("create_at")
            for it in job_full:
                sub_item = {}
                dia_diem=core_models.ThanhPho.objects.get(code=it.dia_diem_lam_viec)
                nghe_nghiep_tin=core_models.NgheNghiep.objects.get(code_job=it.nganh_nghe)
                sub_item['nghe_nghiep'] = nghe_nghiep_tin.name_job
                sub_item['congty'] = it.congty.ten_cong_ty
                sub_item['dia_diem'] = dia_diem.name
                sub_item['muc_luong'] = convert_price_to_string(it.muc_luong)
                sub_item['caption_tin_tuc'] = it.caption_tin_tuc
                sub_item['slug'] = it.slug
                sub_item['ngay_het_han'] = it.ngay_het_han
                list_full.append(sub_item)
        else:
            job_full=None

        if len(list_full) < 10:
            list_full = list_full      
        else:
            paginator = Paginator(list_full, 9)
            page_number = request.GET.get('page')
            list_full = paginator.get_page(page_number)

        context={
            'list_nghe_nghiep':nghe_nghiep,
            'list_thanh_pho':thanh_pho,
            'type_page':2,
            'job_full':job_full,
            'list_full':list_full
        }
        return render(request, 'job_detail/job_full.html',context)


class ListJobViewMana(View):
    def get(self, request):
        nghe_nghiep=core_models.NgheNghiep.objects.all().order_by("name_job")
        thanh_pho=core_models.ThanhPho.objects.all().order_by("name")
        list_mana=[]
        if TinTuyenDung.objects.filter(status_tin=1).order_by("create_at").exists():
            job_mana=TinTuyenDung.objects.filter(status_tin=1).order_by("create_at")
            for it in job_mana:
                sub_item = {}
                dia_diem=core_models.ThanhPho.objects.get(code=it.dia_diem_lam_viec)
                nghe_nghiep_tin=core_models.NgheNghiep.objects.get(code_job=it.nganh_nghe)
                sub_item['nghe_nghiep'] = nghe_nghiep_tin.name_job
                sub_item['congty'] = it.congty.ten_cong_ty
                sub_item['dia_diem'] = dia_diem.name
                sub_item['muc_luong'] = convert_price_to_string(it.muc_luong)
                sub_item['caption_tin_tuc'] = it.caption_tin_tuc
                sub_item['slug'] = it.slug
                sub_item['ngay_het_han'] = it.ngay_het_han
                list_mana.append(sub_item)
        else:
            job_mana=None

        if len(list_mana) < 10:
            list_mana = list_mana      
        else:
            paginator = Paginator(list_mana, 9)
            page_number = request.GET.get('page')
            list_mana = paginator.get_page(page_number)

        context={
            'list_nghe_nghiep':nghe_nghiep,
            'list_thanh_pho':thanh_pho,
            'type_page':1,
            'job_mana':job_mana,
            'list_mana':list_mana
        }



        return render(request, 'job_detail/job_mana.html',context)


class ListJobViewFree(View):
    def get(self, request):
        nghe_nghiep=core_models.NgheNghiep.objects.all().order_by("name_job")
        thanh_pho=core_models.ThanhPho.objects.all().order_by("name")
        list_free=[]
        if TinTuyenDung.objects.filter(Q(status_tin=1,hinh_thuc_lam_viec=6)).order_by("create_at").exists():
            job_free=TinTuyenDung.objects.filter(Q(status_tin=1,hinh_thuc_lam_viec=6)).order_by("create_at")
            for it in job_free:
                sub_item = {}
                dia_diem=core_models.ThanhPho.objects.get(code=it.dia_diem_lam_viec)
                nghe_nghiep_tin=core_models.NgheNghiep.objects.get(code_job=it.nganh_nghe)
                sub_item['nghe_nghiep'] = nghe_nghiep_tin.name_job
                sub_item['congty'] = it.congty.ten_cong_ty
                sub_item['dia_diem'] = dia_diem.name
                sub_item['muc_luong'] = convert_price_to_string(it.muc_luong)
                sub_item['caption_tin_tuc'] = it.caption_tin_tuc
                sub_item['slug'] = it.slug
                sub_item['ngay_het_han'] = it.ngay_het_han
                list_free.append(sub_item)
        else:
            job_free=None

        if len(list_free) < 10:
            list_free = list_free      
        else:
            paginator = Paginator(list_free, 9)
            page_number = request.GET.get('page')
            list_free = paginator.get_page(page_number)

        context={
            'list_nghe_nghiep':nghe_nghiep,
            'list_thanh_pho':thanh_pho,
            'type_page':3,
            'job_free':job_free,
            'list_free':list_free
        }

        return render(request, 'job_detail/job_free.html',context)


class ListJobViewPart(View):
    def get(self, request):
        nghe_nghiep=core_models.NgheNghiep.objects.all().order_by("name_job")
        thanh_pho=core_models.ThanhPho.objects.all().order_by("name")
        list_part=[]
        if TinTuyenDung.objects.filter(Q(status_tin=1,hinh_thuc_lam_viec=3) | Q(status_tin=1,hinh_thuc_lam_viec=4) ).order_by("create_at").exists():
            job_part=TinTuyenDung.objects.filter(Q(status_tin=1,hinh_thuc_lam_viec=3) | Q(status_tin=1,hinh_thuc_lam_viec=4) ).order_by("create_at")
            for it in job_part:
                sub_item = {}
                dia_diem=core_models.ThanhPho.objects.get(code=it.dia_diem_lam_viec)
                nghe_nghiep_tin=core_models.NgheNghiep.objects.get(code_job=it.nganh_nghe)
                sub_item['nghe_nghiep'] = nghe_nghiep_tin.name_job
                sub_item['congty'] = it.congty.ten_cong_ty
                sub_item['dia_diem'] = dia_diem.name
                sub_item['muc_luong'] = convert_price_to_string(it.muc_luong)
                sub_item['caption_tin_tuc'] = it.caption_tin_tuc
                sub_item['slug'] = it.slug
                sub_item['ngay_het_han'] = it.ngay_het_han
                list_part.append(sub_item)
        else:
            job_part=None

        if len(list_part) < 10:
            list_part = list_part      
        else:
            paginator = Paginator(list_part, 9)
            page_number = request.GET.get('page')
            list_part = paginator.get_page(page_number)

        context={
            'list_nghe_nghiep':nghe_nghiep,
            'list_thanh_pho':thanh_pho,
            'type_page':4,
            'job_part':job_part,
            'list_part':list_part
        }

        return render(request, 'job_detail/job_part.html',context)


class HoSoView(LoginRequiredMixin,View):
    login_url = '/dang-nhap/'
    def get(self, request):
        nghe_nghiep=core_models.NgheNghiep.objects.all().order_by("name_job")
        thanh_pho=core_models.ThanhPho.objects.all().order_by("name")
        user=User.objects.get(id=request.user.id)
        if user.loai_user == 2:
            logout(request)
            context={'list_nghe_nghiep':nghe_nghiep,'list_thanh_pho':thanh_pho,'user':user}
            return render(request, 'job_detail/yeu_cau_login.html',context)
        else:
            if seeker_models.HoSoUngTuyen.objects.filter(user=request.user).exists():
                hoso=seeker_models.HoSoUngTuyen.objects.get(user=user)
                context={
                    'list_nghe_nghiep':nghe_nghiep,
                    'list_thanh_pho':thanh_pho,
                    'hoso':hoso,
                    'user':user,
                    'gt':convert_sex(user.gender), 
                    'tthn':convert_tthn(hoso.hon_nhan),
                    'hoc_van':convert_hocvan(hoso.trinh_do_hoc_van),
                    'hinh_thuc':convert_hinhthuc(hoso.hinh_thuc_lam_viec),
                    'td_nn':convert_trinhdo(hoso.trinh_do_ngoai_ngu),
                    'nn':convert_ngoaingu(hoso.ngoai_ngu)
                }
            else:
                context={
                    'list_nghe_nghiep':nghe_nghiep,
                    'list_thanh_pho':thanh_pho,
                    'user':user,
                }
            return render(request, 'job_detail/hoso.html',context)


class SearchJobView(View):
    def get(self, request):
        nghe_nghiep=core_models.NgheNghiep.objects.all().order_by("name_job")
        thanh_pho=core_models.ThanhPho.objects.all().order_by("name")
        context={
            'list_nghe_nghiep':nghe_nghiep,
            'list_thanh_pho':thanh_pho,
        }
        return render(request, 'job_detail/search.html',context)


class SubmitInfoAccAPI(APIView):
    permission_classes = (permissions.AllowAny, )
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer, )
    def post(self, request, format=None):
        valid_data = validate_data(seeker_serializers.SubmitInfoAccAPISer, request.data)
        ten_day_du = valid_data.get('ten_day_du')
        dien_thoai_lien_he = valid_data.get('dien_thoai_lien_he')
        ngay_sinh = valid_data.get('ngay_sinh')
        dia_chi_lien_he = valid_data.get('dia_chi_lien_he')
        thanh_pho_song = int(valid_data.get('thanh_pho_song'))
        gioi_tinh = int(valid_data.get('gioi_tinh'))
        tinh_trang_hn = int(valid_data.get('tinh_trang_hn'))
        if ten_day_du == "" or dien_thoai_lien_he == "" or ngay_sinh == "" or dia_chi_lien_he == "" or thanh_pho_song == 0:
            return Response(data={"err":2}, status=status.HTTP_200_OK)
        else:
            user = User.objects.get(id=request.user.id)
            if user.loai_user == 1:
                user.fullname=ten_day_du
                user.gender=gioi_tinh
                user.birth_day=ngay_sinh
                user.dia_chi_tinh_thanh_pho=thanh_pho_song
                user.dia_chi_chi_tiet=dia_chi_lien_he
                user.sdt=dien_thoai_lien_he
                user.save()
                if seeker_models.HoSoUngTuyen.objects.filter(user=request.user).exists():
                    hoso=seeker_models.HoSoUngTuyen.objects.get(user=user)
                else:
                    hoso=seeker_models.HoSoUngTuyen.objects.create(user=user)
                hoso.hon_nhan=tinh_trang_hn
                hoso.save()
            return Response(data={"err":1,'gt':convert_sex(gioi_tinh) , 'tthn':convert_tthn(tinh_trang_hn)}, status=status.HTTP_200_OK)


class SubmitInfoNormalAPI(APIView):
    permission_classes = (permissions.AllowAny, )
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer, )
    def post(self, request, format=None):
        valid_data = validate_data(seeker_serializers.SubmitInfoNormalAPISer, request.data)
        vi_tri = valid_data.get('vi_tri')
        nganh_nghe = valid_data.get('nganh_nghe')
        thanh_pho_lv = valid_data.get('thanh_pho_lv')
        trinh_do = valid_data.get('trinh_do')
        nam_kn = valid_data.get('nam_kn')
        hinhthuc_lv = valid_data.get('hinhthuc_lv')
        luong_sal = valid_data.get('luong_sal')

        if vi_tri == "" or nganh_nghe == 0 or thanh_pho_lv == 0 or trinh_do == 0 or nam_kn == 0 or hinhthuc_lv == 0 or luong_sal == "":
            return Response(data={"err":2}, status=status.HTTP_200_OK)
        else:
            user = User.objects.get(id=request.user.id)
            if seeker_models.HoSoUngTuyen.objects.filter(user=request.user).exists():
                hoso=seeker_models.HoSoUngTuyen.objects.get(user=user)
            else:
                hoso=seeker_models.HoSoUngTuyen.objects.create(user=user)
            hoso.nganh_nghe=nganh_nghe
            hoso.vi_tri_mong_muon=vi_tri
            hoso.dia_diem_lam_viec=thanh_pho_lv
            hoso.trinh_do_hoc_van=trinh_do
            hoso.so_nam_kinh_nghiem=nam_kn
            hoso.hinh_thuc_lam_viec=hinhthuc_lv
            hoso.muc_luong_toi_thieu=luong_sal
            hoso.save()
            data={
                "err":1,
                'hoc_van':convert_hocvan(hoso.trinh_do_hoc_van),
                'hinh_thuc':convert_hinhthuc(hoso.hinh_thuc_lam_viec),
                'td_nn':convert_trinhdo(hoso.trinh_do_ngoai_ngu)
            }
            return Response(data=data, status=status.HTTP_200_OK)


class SubmitInfoExpAPI(APIView):
    permission_classes = (permissions.AllowAny, )
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer, )
    def post(self, request, format=None):
        valid_data = validate_data(seeker_serializers.SubmitInfoExpAPISer, request.data)
        cty_lv = valid_data.get('cty_lv')
        bang_cap = valid_data.get('bang_cap')
        dao_tao = valid_data.get('dao_tao')
        chuyen_nganh = valid_data.get('chuyen_nganh')
        bat_dau = valid_data.get('bat_dau')
        ket_thuc = valid_data.get('ket_thuc')
        loai_tot_nghiep = valid_data.get('loai_tot_nghiep')

        if cty_lv == "" or bang_cap == "" or dao_tao == "" or chuyen_nganh == "" or bat_dau == "0" or ket_thuc == "0" or ket_thuc == 0:
            return Response(data={"err":2}, status=status.HTTP_200_OK)
        else:
            user = User.objects.get(id=request.user.id)
            if seeker_models.HoSoUngTuyen.objects.filter(user=request.user).exists():
                hoso=seeker_models.HoSoUngTuyen.objects.get(user=user)
            else:
                hoso=seeker_models.HoSoUngTuyen.objects.create(user=user)
            hoso.ten_cty_tung_lam=cty_lv
            hoso.ten_bang_cap=bang_cap
            hoso.don_vi_dao_tao=dao_tao
            hoso.chuyen_nganh=chuyen_nganh
            hoso.thoi_gian_bat_dau=bat_dau
            hoso.thoi_gian_ket_thuc=ket_thuc
            hoso.loai_tot_nghiep=loai_tot_nghiep
            hoso.save()
            return Response(data={"err":1}, status=status.HTTP_200_OK)


class SubmitInfoNgoaiNguAPI(APIView):
    permission_classes = (permissions.AllowAny, )
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer, )
    def post(self, request, format=None):
        valid_data = validate_data(seeker_serializers.SubmitInfoNgoaiNguAPISer, request.data)
        ngoai_ngu = valid_data.get('ngoai_ngu')
        trinh_do_nn = valid_data.get('trinh_do_nn')
        ky_nang = valid_data.get('ky_nang')
        so_thich = valid_data.get('so_thich')


        if ngoai_ngu == "" or trinh_do_nn == 0 or ky_nang == "" or so_thich == "":
            return Response(data={"err":2}, status=status.HTTP_200_OK)
        else:
            user = User.objects.get(id=request.user.id)
            if seeker_models.HoSoUngTuyen.objects.filter(user=request.user).exists():
                hoso=seeker_models.HoSoUngTuyen.objects.get(user=user)
            else:
                hoso=seeker_models.HoSoUngTuyen.objects.create(user=user)
            hoso.ngoai_ngu=ngoai_ngu
            hoso.trinh_do_ngoai_ngu=trinh_do_nn
            hoso.ky_nang=ky_nang
            hoso.so_thich=so_thich
            hoso.save()
            return Response(data={"err":1,'tdnn':convert_trinhdo(hoso.trinh_do_ngoai_ngu),'nn_lv':convert_ngoaingu(hoso.ngoai_ngu)}, status=status.HTTP_200_OK)


class SubmitDuyetHoSoAPI(APIView):
    permission_classes = (permissions.AllowAny, )
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer, )
    def post(self, request, format=None):
        valid_data = validate_data(seeker_serializers.SubmitDuyetHoSoAPISer, request.data)
        mana = valid_data.get('mana')

        user = User.objects.get(id=request.user.id)
        if seeker_models.HoSoUngTuyen.objects.filter(user=request.user).exists():
            hoso=seeker_models.HoSoUngTuyen.objects.get(user=user)
            # tao ma ho so
            hoso.code_hoso = unique_order_id_generator(request.user.username,1)
            hoso.save()
            gui_hoso_mana.delay(hoso.id)
            return Response(1, status=status.HTTP_200_OK)
        else:
            return Response(1, status=status.HTTP_404_NOT_FOUND)


class DetailJobView(View):
    def get(self, request, slug):
        nghe_nghiep=core_models.NgheNghiep.objects.all().order_by("name_job")
        thanh_pho=core_models.ThanhPho.objects.all().order_by("name")
        user=User.objects.get(id=request.user.id)

        tin_td=company_models.TinTuyenDung.objects.get(slug=slug)
        list_it=[]
        sub_item = {}
        dia_diem=core_models.ThanhPho.objects.get(code=tin_td.dia_diem_lam_viec)
        nghe_nghiep_tin=core_models.NgheNghiep.objects.get(code_job=tin_td.nganh_nghe)
        sub_item['caption_tin_tuc'] = tin_td.caption_tin_tuc
        sub_item['code_tin'] = tin_td.code_tin
        sub_item['congty'] =  tin_td.congty.ten_cong_ty
        sub_item['ngay_het_han'] =  tin_td.ngay_het_han
        sub_item['muc_luong'] = convert_price_to_string(tin_td.muc_luong)
        sub_item['so_nam_kinh_nghiem'] =  tin_td.so_nam_kinh_nghiem
        sub_item['trinh_do_hoc_van'] = convert_hocvan(tin_td.trinh_do_hoc_van)
        sub_item['so_luong_tuyen'] =  tin_td.so_luong_tuyen
        sub_item['nghe_nghiep'] = nghe_nghiep_tin.name_job
        sub_item['dia_diem_lam_viec'] =  dia_diem.name
        sub_item['hinh_thuc_lam_viec'] = convert_hinhthuc(tin_td.hinh_thuc_lam_viec)
        sub_item['ngoai_ngu'] = convert_ngoaingu(tin_td.ngoai_ngu)
        sub_item['trinh_do_ngoai_ngu'] = convert_trinhdo(tin_td.trinh_do_ngoai_ngu)
        sub_item['mota_congviec'] = tin_td.mota_congviec
        sub_item['quyenloi_congviec'] = tin_td.quyenloi_congviec
        sub_item['yeucau_congviec'] = tin_td.yeucau_congviec

        sub_item['dia_chi'] = tin_td.congty.dia_chi
        sub_item['sdt_lienhe'] = tin_td.congty.sdt_lienhe
        sub_item['mail_lien_he'] = tin_td.congty.mail_lien_he
        sub_item['name_lien_he'] = tin_td.congty.name_lien_he


        list_it.append(sub_item)
        context={
            'list_provincial':thanh_pho,
            'list_nghe_nghiep':nghe_nghiep,
            'tin_tuyendung':list_it
        }

        return render(request, 'job_detail/job_detail.html',context)


class FeedbackHoSoMana(APIView):
    permission_classes = (permissions.AllowAny, )
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer, )
    def post(self, request, format=None):
        valid_data = validate_data(seeker_serializers.FeedbackHoSoManaSer, request.data)
        ten_day_du = valid_data.get('ten_day_du')

  
        return Response(1, status=status.HTTP_200_OK)
