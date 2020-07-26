from django.urls import path
from .views import IndexView,AddDataThanhPhoAPI, AddDataNgheNghiepAPI, SearchHomeAPI


urlpatterns = [
    path('', IndexView.as_view(), name='index_page'),

    #api
    path('add-data-thanh-pho/', AddDataThanhPhoAPI.as_view(), name='add-data-thanh-pho'),
    path('add-data-nghe/', AddDataNgheNghiepAPI.as_view(), name='add-data-nghe'),
    path('tim-viec-lam-nangcao/', SearchHomeAPI.as_view(), name='tim-viec-lam-nangcao'),

]
