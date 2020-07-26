from django.urls import path
from . import views as company_views

app_name = 'company'


urlpatterns = [
    path('tuyen-dung/', company_views.TuyenDungView.as_view(), name='tuyendung_url'),
    path('tim-kiem-ho-so/', company_views.TimHoSoAPI.as_view(), name='tim-kiem-ho-so'),
    path('danh-sach-ho-so/', company_views.ListHosoView.as_view(), name='danh-sach-ho-so'),
    path('ho-so/<slug:slug>', company_views.DetailHoSoView.as_view(), name='ho-so'),
    path('tao-tin-tuyen-dung/', company_views.TaoTinTuyendungView.as_view(), name='tao-tin-tuyen-dung'),

    path('submit-info-cty/', company_views.SubmitInfoCtyAPI.as_view(), name='submit-info-cty'),
    path('submit-info-normal/', company_views.SubmitInfoNormalAPI.as_view(), name='submit-info-normal'),
    path('submit-info-nn/', company_views.SubmitInfoNgoaiNguAPI.as_view(), name='submit-info-nn'),
    path('submit-duyet-tintd/', company_views.SubmitDuyetTinTuyenDungAPI.as_view(), name='submit-duyet-tintd'),
    path('feedback-tintd/', company_views.FeedbackTinTuyenDungMana.as_view(), name='feedback-tintd'),

]
