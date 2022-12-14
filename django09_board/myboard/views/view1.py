from django.shortcuts import render, redirect
from myboard.models import BoardTab
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from datetime import datetime

# Create your views here.
def mainFunc(request):
    aa="<div><h2>게시판 메인</h2></div>"
    return render(request, 'boardmain.html',{'msg':aa})

def listFunc(request):
    #data_all = BoardTab.objects.all().order_by('-id') #댓글코드 X
    data_all = BoardTab.objects.all().order_by('-gnum','onum') #댓글코드 X
    
    paginator = Paginator(data_all,10)
    page = request.GET.get('page')
    
    try:
        datas = paginator.page(page)
    except PageNotAnInteger:
        datas = paginator.page(1)
    except EmptyPage:
        datas = paginator.page(paginator.num_pages)
        
    return render(request, 'board.html',{'datas':datas})

def insertFunc(request):
    return render(request, 'insert.html')

def insertOkFunc(request):
    if request.method == "POST":
        try:
            gbun = 1 #Group number 구하기
            datas = BoardTab.objects.all()
            if datas.count() != 0:
                gbun = BoardTab.objects.latest('id').id +1 #0이 아니면 1을 더한다.
            
            BoardTab(
                name = request.POST.get('name'),
                passwd = request.POST.get('passwd'),
                mail = request.POST.get('mail'),
                title = request.POST.get('title'),
                cont = request.POST.get('cont'),
                bip = request.META['REMOTE_ADDR'], #글을 입력한 사람의 주소를 얻을 수 있다.
                bdate = datetime.now(),
                readcnt = 0,
                gnum = gbun,
                onum = 0,
                nested = 0
            ).save()
        except Exception as e:
            print('insert err: ',e)
            return render(request, 'error.html')
    
    return redirect('/board/list')
    
def updateFunc(request):
    try:
        data=BoardTab.objects.get(id=request.GET.get('id'))
    except Exception as e:
        return render(request, 'error.html')
    
    return render(request, 'update.html', {'data_one':data})

def updateOkFunc(request):
    try:
        upRec = BoardTab.objects.get(id=request.POST.get('id')) #db에서 읽었어.
        #비밀번호 비교 / 비교 후 수정여부 결정
        if upRec.passwd == request.POST.get('up_passwd'): #비밀번호가 같으면
            upRec.name = request.POST.get('name')
            upRec.mail = request.POST.get('mail')
            upRec.title = request.POST.get('title')
            upRec.cont = request.POST.get('cont')
            upRec.save()
        else:
            return render(request, 'update.html', {'data_one':upRec, 'msg':'비밀번호 불일치'})
    except Exception as e:
        return render(request, 'error.html')
          
    return redirect('/board/list')   

def searchFunc(request):
    if request.method == 'POST':
        s_type = request.POST.get('s_type')
        s_value = request.POST.get('s_value')
        #print(s_type, s_value) 잘 들어오나 확인
        #SQL의 like 연산 -- ORM에서는 __contain=값
        if s_type == 'title':
            datas_search = BoardTab.objects.filter(title__contains=s_value).order_by('-id')
        elif s_type == 'name':
            datas_search = BoardTab.objects.filter(name__contains=s_value).order_by('-id')

        paginator = Paginator(datas_search,5)
        page = request.GET.get('page')
        
        try:
            datas = paginator.page(page)
        except PageNotAnInteger:
            datas = paginator.page(1)
        except EmptyPage:
            datas = paginator.page(paginator.num_pages)
            
        return render(request, 'board.html',{'datas':datas})


def contentFunc(request):
    page = request.GET.get('page')
    data = BoardTab.objects.get(id=request.GET.get('id'))
    data.readcnt = data.readcnt +1  #그냥 조회수 증가
    data.save() #조회수 update(갱신함)
    
    return render(request, 'content.html', {'data_one':data, 'page':page})

def deleteFunc(request):
    try:
        del_data=BoardTab.objects.get(id=request.GET.get('id'))
    except Exception as e:
        return render(request, 'error.html')
    
    return render(request, 'delete.html', {'data_one':del_data})

def deleteOkFunc(request):
    del_data = BoardTab.objects.get(id=request.POST.get('id'))
    
    if del_data.passwd == request.POST.get('del_passwd'):
        del_data.delete();
        
        return redirect('/board/list')
    
    else:
        return render(request, 'error.html')