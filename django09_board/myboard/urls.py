from django.urls import path
from myboard.views import view1, view2

urlpatterns = [
    path('list', view1.listFunc),
    
    path('insert',view1.insertFunc),
    path('insertok',view1.insertOkFunc),
    
    path('update',view1.updateFunc), 
    path('updateok',view1.updateOkFunc),
    
    path('search',view1.searchFunc), #검색
    
    path('content',view1.contentFunc), #상세보기
    
    path('delete',view1.deleteFunc),
    path('deleteok',view1.deleteOkFunc),
    
    #답글관련
    path('reply',view2.replyFunc),
    path('replyok',view2.replyOkFunc), 
]