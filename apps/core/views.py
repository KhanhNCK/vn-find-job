from django.shortcuts import render, redirect
from rest_framework.views import exception_handler as drf_exception_handler
from django.views import View
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.views import APIView
from rest_framework import permissions,status
from apps.core.utils import validate_data, validate_response ,convert_price_to_string 
from . import models as core_models
from . import serializers as core_serializers
import json
import requests
from apps.company import models as company_models

# Create your views here.


def exception_handler(exc, context):
    response = drf_exception_handler(exc, context)
    return response


def Error404Page(request, exception):
    return render(request, 'error_pages/page_403.html')


def Error500Page(request):
    return render(request, 'error_pages/page_500.html')


def Error403Page(request, exception):
    return render(request, 'error_pages/page_403.html')


class IndexView(View):
    def get(self, request):
        nghe_nghiep=core_models.NgheNghiep.objects.all().order_by("name_job")
        thanh_pho=core_models.ThanhPho.objects.all().order_by("name")
        context={
            'list_nghe_nghiep':nghe_nghiep,
            'list_thanh_pho':thanh_pho
        }
        return render(request, 'core/index.html',context)


class AddDataThanhPhoAPI(APIView):
    permission_classes = (permissions.AllowAny, )
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer, )
    def post(self, request, format=None):
        valid_data = validate_data(core_serializers.AddDataThanhPhoAPISer, request.data)

        name = valid_data.get('name')
        code = valid_data.get('code')
        group = valid_data.get('group')
        longitude = valid_data.get('longitude')
        latitude = valid_data.get('latitude')
        if core_models.ThanhPho.objects.filter(name=name,code=code, group = group,longitude=longitude,latitude=latitude).exists():
            return Response(1, status=status.HTTP_400_BAD_REQUEST)
        else:
            gsp = core_models.ThanhPho.objects.create(name=name,code=code, group = group,longitude=longitude,latitude=latitude)
            return Response(1, status=status.HTTP_200_OK)


class AddDataNgheNghiepAPI(APIView):
    permission_classes = (permissions.AllowAny, )
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer, )
    def post(self, request, format=None):
        valid_data = validate_data(core_serializers.AddDataNgheNghiepAPISer, request.data)

        name_job = valid_data.get('name_job')
        job_info = valid_data.get('job_info')
        code_job = int(valid_data.get('code_job'))

        if core_models.NgheNghiep.objects.filter(name_job=name_job,job_info=job_info, code_job = code_job).exists():
            return Response(1, status=status.HTTP_400_BAD_REQUEST)
        else:
            core_models.NgheNghiep.objects.create(name_job=name_job,job_info=job_info, code_job = code_job)
            return Response(1, status=status.HTTP_200_OK)


class SearchHomeAPI(APIView):
    permission_classes = (permissions.AllowAny, )
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer, )
    def post(self, request, format=None):
        valid_data = validate_data(core_serializers.SearchHomeAPISer, request.data)

        key_job = valid_data.get('key_job')
        nganh_nghe = int(valid_data.get('nganh_nghe'))
        thanh_pho = int(valid_data.get('thanh_pho'))

        # if nganh_nghe == 0:
        #     if thanh_pho == 0:
        #         tintd=company_models.TinTuyenDung.objects.filter(tag_search__unaccent__icontains=key_job)
        #     else:
        #         tintd=company_models.TinTuyenDung.objects.filter(dia_diem_lam_viec=thanh_pho)
        # else:
        #     tintd=company_models.TinTuyenDung.objects.filter(nganh_nghe=nganh_nghe)


        # request.session['tintuyendung_find'] = tintd

        return Response(1, status=status.HTTP_200_OK)