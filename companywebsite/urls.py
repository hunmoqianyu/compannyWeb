"""companywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from django.views.static import serve

from companywebsite import settings
from website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    re_path(r'^product/(?P<product_pk>\d+)/$', views.product, name='product'),
    path('profile', views.profile, name='profile'),
    path('contact', views.contact, name='contact'),
    path('feedback', views.feedback, name='feedback'),
    path('clients', views.clients, name='clients'),
    path('support', views.support, name='support'),
    path('download', views.download, name='download'),
    path('aft_sale', views.aft_sale, name='aft_sale'),
    path('problems', views.problems, name='download'),
    path('success_case', views.suc_case, name='suc_case'),
    path('custom_made', views.custom_made, name='custom_made'),
    url(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}, name='static'),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


