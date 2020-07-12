from django.urls import path
from . import views as user_views

urlpatterns = [
    path('login/', user_views.LoginAPIView.as_view()),
    path('login_history/', user_views.GetUserInfoAPIView.as_view()),
    path('dang-xuat/', user_views.LogoutView.as_view(), name='logout_url'),
    path('dang-nhap/',user_views.LoginView.as_view(), name='login_url'),
    path('dang-ky/', user_views.RegisterView.as_view(), name='register_url'),

]
