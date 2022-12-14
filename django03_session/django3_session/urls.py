"""django3_session URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from sessionapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    #얘네들은 클라이언트를 통해서 호출할 때만 만날 수 있다.
    path('',views.mainFunc),
    path('setos',views.setOsFunc),
    path('showos',views.showOsFunc), 
]
