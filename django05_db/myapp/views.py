from django.shortcuts import render
from myapp.models import Article

# Create your views here.
def main(request):
    return render(request, 'main.html')

def show(request):
    # sql="select * from Article" #이건 내부적으로 돌아간다
    datas=Article.objects.all()  #이것이 바로 Django ORM
    print(datas)
    print(datas[0].name)
    return render(request,"list.html",{"articles":datas})