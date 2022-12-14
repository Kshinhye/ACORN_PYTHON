from django.shortcuts import render
import MySQLdb
from mysangpum.models import Sangdata
from django.http.response import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def ListFunc(request):
    '''
    #sql문 직접사용
    sql="SELECT * FROM sangdata"
    conn=MySQLdb.connect(**config)
    cursor=conn.cursor()
    cursor.execute(sql)
    datas=cursor.fetchall()
    print(datas,type(datas)) #반환타입:tuple
    
    위 코드 또는 아래 코드 
    
    #ORM사용 반환타입:QuerySet
    datas=Sangdata.objects.all()
    return render(request,'list.html',{'sangpums':datas})
    '''
    
    # 페이지 나누기--------------
    datas=Sangdata.objects.all().order_by('-code')
    paginator=Paginator(datas, 5)
    try:
        page=request.GET.get('page')
    except:
        page=1
    
    try:
        data=paginator.page(page) #해당 페이지 자료를 받는다.
        
    except PageNotAnInteger:
        data=paginator.page(1)
        
    except EmptyPage:
        data=paginator.page(paginator.num_pages()) 
        
    #낱개 페이지 번호를 출력한다면...
    allpage=range(paginator.num_pages +1) #(0,4 +1)
        
    return render(request,'list2.html',{'sangpums':data,'allpage':allpage})


def InsertFunc(request):
    return render(request,'insert.html')

def InsertOkFunc(request):
    if request.method == 'POST':
        #신상품 code 등록 여부 판단
        try:
            Sangdata.objects.get(code=request.POST.get('code'))
            return render(request,'insert.html',{'msg':'이미 등록 된 code입니다.'}) #없다면 얘한테 보낸다.
        except Exception as e:
            #등록된 입력자료의 code가 등록된 숫자가 아니므로 insert 작업을 진행
            Sangdata(
                code=request.POST.get('code'),
                sang=request.POST.get('sang'),
                su=request.POST.get('su'),
                dan=request.POST.get('dan'),
            ).save()
            
        return HttpResponseRedirect('/sangpum/list') #추가 후 목록보기

def UpdateFunc(request):
    data = Sangdata.objects.get(code=request.GET.get('code')) 
    return render(request, 'update.html',{'sang_one':data})


def UpdateOkFunc(request):
    if request.method == 'POST':
        upRec=Sangdata.objects.get(code=request.POST.get('code'))
        upRec.code=request.POST.get('code')
        upRec.sang=request.POST.get('sang')
        upRec.su=request.POST.get('su')
        upRec.dan=request.POST.get('dan')
        upRec.save()

    return HttpResponseRedirect('/sangpum/list') #수정 후 목록보기

def DeleteFunc(request):
    delRec=Sangdata.objects.get(code=request.GET.get('code'))
    delRec.delete()
    return HttpResponseRedirect('/sangpum/list') #삭제 후 목록보기
