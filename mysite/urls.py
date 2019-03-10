"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from myapp import views
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('',views.index, name='index'),
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('user_preference/', views.userPreference, name='user_preference'),
    path('smart_list/', views.smartList, name='smart_list'),
    path('get_branches/', views.getBranches, name='get_branches'),
    path('export_pdf/', views.export_pdf, name='export_pdf'),
]
