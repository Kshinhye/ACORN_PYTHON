from django.urls import path
from myguest import views

urlpatterns = [
    path('select', views.ListFunc), 
    path('insert',views.InsertFunc),
    path('insertok',views.InsertOkFunc), 
]