from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.core.models import ThanhPho
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.views import APIView
from rest_framework import permissions,status
from apps.core.utils import validate_data, validate_response ,convert_price_to_string 
from . import models as company_models
from . import serializers as company_serializers
# Create your views here.


class TuyenDungView(LoginRequiredMixin,View):
    login_url = '/dang-nhap/'
    def get(self, request):
        list_provincial=ThanhPho.objects.all().order_by("name")
        context={
            'list_provincial':list_provincial
        }

        return render(request, 'company/tuyendung.html',context)


class TimHoSoAPI(APIView):
    permission_classes = (permissions.AllowAny, )
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer, )
    def post(self, request, format=None):
        valid_data = validate_data(company_serializers.TimHoSoAPI, request.data)

        # name = valid_data.get('name')
        # code = valid_data.get('code')
        # group = valid_data.get('group')
        # longitude = valid_data.get('longitude')
        # latitude = valid_data.get('latitude')
        
        return Response(1, status=status.HTTP_200_OK)