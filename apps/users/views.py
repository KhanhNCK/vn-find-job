from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from apps.core.utils import validate_data,validate_response
from django.contrib.auth import authenticate, login
from apps.core.exceptions import HTTP401AuthenticationError, HTTP404NotFoundError, HTTP409ConflictError
from .models import LoginHistory,User
from django.views import View
from django.contrib.auth import logout
from django.core.cache import cache
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
import json
import requests
from . import models as user_models
from . import utils as user_utils
from . import serializers as user_sers
from .forms import LoginForm
import urllib.request
from django.conf import settings
from datetime import datetime
import pytz
from django.utils import timezone
from datetime import timedelta




class LoginAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        valid_data = validate_data(user_sers.LoginEmailValidator, request.data)

        username = valid_data.get('username')
        password = valid_data.get('password')
        user = authenticate(username=username, password=password)

        if not user:
            raise HTTP401AuthenticationError('Incorrect email or password1')

        access_token = user_models.generate_access_token(user.id)
        token = user_models.Token.objects.create(user=user, key=access_token)
        data = {
            'id': user.id,
            'username': user.id,
            'email': user.id,
            'access_token': token.key,
        }

        user_utils.create_or_update_login_history(user.id)
        serializer = user_sers.TokenSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetUserInfoAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request):
        his = LoginHistory.objects.all()
        ser = user_sers.LoginHistorySerializer(his, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)


class LogoutAPI(APIView):

    def post(self, request, format=None):
        user_models.Token.objects.filter(key=request.auth.key).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GetAllUser(APIView):

    def get(self, request, format=None):
        pass


class LoginView(View):

    def get(self, request):
        message = ''
        fm = LoginForm()
        context = {'f': fm, 'message': message}
        return render(request, 'core/login.html', context)

    def post(self, request):
        #test_func.delay()
        login_valid = LoginForm(request.POST)
        fm = LoginForm()
        message = "Đăng nhập thất bại"
        message2 = "( tài khoản hoặc mật khẩu bạn nhập không đúng )"
        context = {'f': fm, 'message': message, 'message2': message2 }

        redirect_to = request.GET.get('next', '') 

        if login_valid.is_valid():
            username = login_valid.cleaned_data['username']
            password = login_valid.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if not user:
                return render(request, 'core/login.html', context)
            login(request, user)
            if redirect_to == '':
                return redirect('index_page')
            return redirect(redirect_to)
        else:
            return render(request, 'core/login.html', context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index_page')


class RegisterView(View):
    def get(self, request):
        # full_link_info = request.build_absolute_uri()
        # # print("khanh=",full_link_info)
        # ref_url = request.GET.get('ref')
        # if not ref_url:
        #     return render(request, 'core/register.html')
        # elif not User.objects.filter(link_info=full_link_info).exists():
        #     context={'message':"Link giới thiệu bạn nhập không chính xác"}
        #     return render(request, 'core/register.html',context)
        # context={'ref_url': ref_url}
        return render(request, 'core/register.html')

    def post(self, request):
        # phone = request.POST.get('phone_number')
        # password1 = request.POST.get('password')
        # password2 = request.POST.get('repassword')
        # ref_url1 = request.POST.get('id_person_invite')

        # if password1 != password2:
        #     msg = {'message':'Bạn nhập lại mật khẩu không chính xác'}
        #     return render(request, 'core/register.html', msg)

        # if User.objects.filter(username=phone, is_active=True).exists():
        #     msg = {'message':'Tài khoản này đã tồn tại'}
        #     return render(request, 'core/register.html', msg)

        # if not User.objects.filter(username=phone, is_active=False).exists():
        #     user =  User.objects.create_user(username=phone, email=None, password=password1, is_active=False)
        #     user.code_invite=ref_url1
        #     user.save()

        # if User.objects.filter(username=phone, is_active=False).exists():
        #     request.session['phone_number'] = phone
        #     otp_code = user_utils.generate_otp_code()
        #     cache.set(phone, otp_code, timeout=300)
        #     get_ip = get_client_ip(request)
        #     if user_models.CountOTP.objects.filter(phone_otp=phone, count_otp__gte=5, ip_client=get_ip).exists():
        #         msg = {'message':'Bạn nhập quá số lần cho phép'}
        #         return render(request, 'core/index-ver2.html',msg)
        #     else:
        #         # otp_status = user_utils.send_otp(phone_number=phone, otp_code=otp_code)
        #         if user_models.CountOTP.objects.filter(phone_otp=phone, ip_client=get_ip).exists():
        #             count = user_models.CountOTP.objects.filter(phone_otp=phone, ip_client=get_ip).first()
        #             count.count_otp += 1
        #             count.save()
        #         else:
        #             user_models.CountOTP.objects.create(phone_otp=phone, ip_client=get_ip, count_otp=1)
        #         otp_status=200
        #         otp_status2 = 0
        #         if otp_status != 200:
        #             otp_status2 = user_utils.send_voic_call(phone_number=phone, otp_code=otp_code)
        #         if otp_status == 200 or otp_status2 == 200:
        #             return redirect('otp_verify')

        #send otp
        # print('so dien thoai1: ', phone)
        # print('otp1 = ', otp_code)
        return render(request, 'core/register.html')
