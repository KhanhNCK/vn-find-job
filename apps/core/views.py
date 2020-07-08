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
        return render(request, 'core/index.html')


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

        ten_nganh_nghe = valid_data.get('ten_nganh_nghe')
        code_nganh_nghe = valid_data.get('code_nganh_nghe')
        thong_tin_ve_nghe = valid_data.get('thong_tin_ve_nghe')

        if core_models.NgheNghiep.objects.filter(ten_nganh_nghe=ten_nganh_nghe,code_nganh_nghe=code_nganh_nghe, thong_tin_ve_nghe = thong_tin_ve_nghe).exists():
            return Response(1, status=status.HTTP_400_BAD_REQUEST)
        else:
            gsp = core_models.NgheNghiep.objects.create(ten_nganh_nghe=ten_nganh_nghe,code_nganh_nghe=code_nganh_nghe, thong_tin_ve_nghe = thong_tin_ve_nghe)
            return Response(1, status=status.HTTP_200_OK)  