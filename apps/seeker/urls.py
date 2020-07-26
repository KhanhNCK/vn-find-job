from django.urls import path
from . import views as seeker_views

app_name = 'seeker'


urlpatterns = [
    path('viec-lam-fulltime/', seeker_views.ListJobViewFull.as_view(), name='viec_lam_full'),
    path('viec-lam-quan-ly/', seeker_views.ListJobViewMana.as_view(), name='viec_lam_mana'),
    path('viec-lam-freelandcer/', seeker_views.ListJobViewFree.as_view(), name='viec_lam_free'),
    path('viec-lam-parttime/', seeker_views.ListJobViewPart.as_view(), name='viec_lam_part'),

    path('tao-ho-so/', seeker_views.HoSoView.as_view(), name='tao_hoso_url'),
    path('tim-kiem-viec-lam/', seeker_views.SearchJobView.as_view(), name='find_job'),
    path('submit-info-acc/', seeker_views.SubmitInfoAccAPI.as_view(), name='submit-info-acc'),
    path('submit-info-normal/', seeker_views.SubmitInfoNormalAPI.as_view(), name='submit-info-normal'),
    path('submit-info-exp/', seeker_views.SubmitInfoExpAPI.as_view(), name='submit-info-exp'),
    path('submit-info-nn/', seeker_views.SubmitInfoNgoaiNguAPI.as_view(), name='submit-info-nn'),
    path('submit-duyeths/', seeker_views.SubmitDuyetHoSoAPI.as_view(), name='submit-duyeths'),
    path('tin-tuyen-dung/<slug:slug>/', seeker_views.DetailJobView.as_view(), name='tin_tuyen_dung_url'),
    path('feedback-hoso/', seeker_views.FeedbackHoSoMana.as_view(), name='feedback-hoso'),

]
