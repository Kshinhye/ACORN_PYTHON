from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def indexFunc(request):  #클라이언트의 요청과 맵핑되는 함수
    '''
    msg="DJANGO 'D'는 묵음이야"
    ss="<html><body><h1>장고 프로젝트 처리 : %s</h1></body></html>"%msg
    #return HttpResponse('요청처리')
    return HttpResponse(ss)
    '''
    
    # 클라이언트에세 html 파일을 반환해보자 : 파이썬 값을 html에 담아서 전달
    msg="DJANGO 'D'는 묵음이야"
    context={'msg':msg} #dict type으로 작서해 html 문서에 기술한 장고 template 기호와 매핑
    return render(request, 'main.html', context)  #forward 방식 기본 / 서버가 클라이언트한테 바로 push #렌더링이란?

def helloFunc(request):
    return render(request, 'show.html')