"""django4_shop URL Configuration

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
from basket_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    
    path("",views.mainFunc), #원래는 위임해야하는데 간단하니까 그냥해~
    path("page1",views.page1Func),
    path("page2",views.page2Func), 
    path("cart",views.cartFunc), 
    path("buy",views.buyFunc), 
]
