from django.shortcuts import render, redirect
from myguest.models import Guest
from datetime import datetime
from django.utils import timezone #settings에 TIME_ZONE에서 설정가능
from django.http.response import HttpResponseRedirect

# Create your views here.
def MainFunc(request):
    msg="<h1>홈페이지</h1>" #그냥 써보는거야
    return render(request, 'main.html',{'msg':msg})

def ListFunc(request):
    # print(gdatas)
    # print(Guest.objects.get(id=1))
    # print(Guest.objects.filter(id=1))
    # print(Guest.objects.filter(title='안녕'))
    # print(Guest.objects.filter(title__contains='안녕'))
    
    gdatas=Guest.objects.all()
    # gdatas=Guest.objects.all() #뿌려주기 #gdatas는 쿼리셋 타입이다.4
    ##정렬 sort!!!!!##
    # gdatas=Guest.objects.all().order_by('-id')
    # gdatas=Guest.objects.all().order_by('title') #title별로 정렬할거야 (오름차순)
    # gdatas=Guest.objects.all().order_by('-title') #title별로 정렬할거야 (내림차순)
    # gdatas=Guest.objects.all().order_by('title','-id') #title이 같은 애들끼리에서 id정렬
    # gdatas=Guest.objects.all().order_by('-id')[0:2]

    return render(request, 'list.html',{'gdatas':gdatas})  #gdatas키로 gdatas값을 달고 갈게요~ html에 달고갈 수 있는건 뭐였지

def InsertFunc(request):
    return render(request,'insert.html') #클라이언트가 요청하면 메인 urls가 부르기때문에 일반적으로 파일을 부를 땐 이렇게 포워딩으로 부른다

def InsertOkFunc(request):
    if request.method == 'POST':
        #print(request.POST.get('title')) #잘 넘어오나 확인
        #Guest().save() #콘솔로 넘어오늘걸 확인 했으니 이제 넘어오는 데이터를 저장해보자
        #orm insert 문
        Guest(
            title=request.POST['title'],
            content=request.POST['content'],
            #regdate=datetime.now()
            regdate=timezone.now()
        ).save()
        
    #return HttpResponseRedirect('/guest/select')  #방법1: 추가 후 목록보기 (리다이렉트방식)
    return redirect('/guest/select')  #방법2: 추가 후 목록보기 (리다이렉트방식)