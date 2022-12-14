from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
#Function views
def mainFunc(request): #import하면안된다!!!!!!!!!!기본제공request를 써야해요
    return render(request,'index.html')

#Class-based views
class CallView(TemplateView):  #TemplateView 상속
    template_name = "callget.html" #파일명 하나를 줄게요

#Including another URLconf (위임)
def insertFunc(request):
    return render(request, 'insert.html')

def insertprocessFunc(request):
    if request.method == 'GET':
        irum = request.GET.get("name") #받아주기 (JAVA: request.getParameter("name"))
        print(irum)
        return render(request,'list.html',{'myname': irum})
    
def insertFunc2(request):
    if request.method == 'GET':
        return render(request, 'insert2.html')
    elif request.method == 'POST':
        irum = request.POST.get("name")  #받아주고
        return render(request,'list.html',{'myname': irum}) #넘겨주기
    else:
        print('요청에러')