from django.urls import path
from . import views as seeker_views

app_name = 'seeker'


urlpatterns = [
    path('viec-lam-fulltime/', seeker_views.ListJobViewFull.as_view(), name='viec_lam_full'),
    path('viec-lam-quan-ly/', seeker_views.ListJobViewMana.as_view(), name='viec_lam_mana'),
    path('viec-lam-freelandcer/', seeker_views.ListJobViewFree.as_view(), name='viec_lam_free'),
    path('viec-lam-parttime/', seeker_views.ListJobViewPart.as_view(), name='viec_lam_part'),

    path('ho-so/', seeker_views.HoSoView.as_view(), name='hoso_url'),

]
