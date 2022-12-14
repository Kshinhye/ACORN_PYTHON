from django.shortcuts import render
import time
import json
from django.http.response import HttpResponse

# Create your views here.

lan = {
    'id':123,
    'name':'파이썬',
    'history':[
        {'date':'2022-9-20','exam':'basic'},
        {'date':'2022-10-20','exam':'django'},
    ]
}


#일반 함수
def testFunc():
    print(type(lan))  #<class 'dict'> 얘는 파이썬의 오브젝트
    
    #인코딩디코딩 이야기를 해볼게
    #JSON 인코딩 : Python Object(여기에선 dict(lan))를 문자열str로 변경
    #jsonString = json.dumps(lan)
    jsonString = json.dumps(lan,indent=4)
    print(jsonString)
    print(type(jsonString))  #<class 'str'> 제이쓴
    
    #JSON 디코딩 : JSON 문자열을 Python Object(dict,list,tuple...)로 변경
    dic = json.loads(jsonString)
    print(type(dic))
    print(dic)
    print(dic['name'])
    
#요청에 대해서 반응을 보이는 이벤트핸들러함수 / 함수로 쓸 수도있고 클래스로 쓸 수도 있다.
def indexFunc(request):
    testFunc()
    return render(request, 'abc.html')

def Func1(request):
    msg = request.GET.get('msg')
    msg="nice "+msg
    print(msg)
    context = {'key':msg}
    time.sleep(5) 
    return HttpResponse(json.dumps(context),content_type="application/json") #제이쓴 문자열로 변경

def Func2(request):
    #db에서 받았다고 가정
    datas=[
        {'irum':'홍길동','nai':22},
        {'irum':'청길동','nai':32},
        {'irum':'백길동','nai':42},
    ]
    
    return HttpResponse(json.dumps(datas),content_type="application/json")
