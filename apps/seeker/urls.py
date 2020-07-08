from django.urls import path
from . import views as seeker_views

app_name = 'seeker'


urlpatterns = [
    path('viec-lam/', seeker_views.ListJobView.as_view(), name='viec-lam'),
]
