from django.urls import path
from .views import IndexView,AddDataThanhPhoAPI


urlpatterns = [
    path('', IndexView.as_view(), name='index_page'),

    #api
    path('add-data-nghenghiep', AddDataThanhPhoAPI.as_view(), name='add-data-nghenghiep'),
]
