from django.urls import path
from . import views as company_views

app_name = 'company'


urlpatterns = [
    path('tuyen-dung/', company_views.TuyenDungView.as_view(), name='tuyendung_url'),
]
