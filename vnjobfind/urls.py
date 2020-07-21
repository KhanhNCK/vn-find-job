"""tracking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.users import views as user_views
from django.conf.urls import handler404, handler500 ,handler403

handler404 = "apps.core.views.Error404Page"
handler500 = "apps.core.views.Error500Page"
handler403 = "apps.core.views.Error403Page"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', user_views.LoginAPIView.as_view(), name='login_url'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('apps.core.urls')),
    path('tim-viec-lam/', include('apps.seeker.urls')),
    path('tim-ho-so/', include('apps.company.urls')),
    path('', include('apps.users.urls')),

]
