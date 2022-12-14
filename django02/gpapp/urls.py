from gpapp import views
from django.urls.conf import path

urlpatterns = [
    path('insert',views.insertFunc), #Function views
    path('insertprocess',views.insertprocessFunc),
    
    path('insert2',views.insertFunc2),
]
