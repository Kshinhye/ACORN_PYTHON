from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from hamcrest.core.core.isnone import none

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html') #이건 물리적인 파일

def setOsFunc(request):
    if "favorite_os" in request.GET: #get방식으로 favorite 요청이 들어온다면 "favorite_os"(변수명)
        #print(request.GET.get(favorite_os)) 그냥 GET / GET.get("") 가능
        print(request.GET["favorite_os"])
        
        #key value 넘기기
        #"f_os"라는 키로 session 생성
        request.session["f_os"] = request.GET["favorite_os"] #세션을 만들었따
        
        #누구를 만나게할거야??
        #return render() 형식은 forarding이기 때문에 클라이언트를 통한 요청 불가(=메인의 urls.py를 만날 수 없다.)
        #forwarding 말고 redirect 방식을 사용한다면 가능함
        return HttpResponseRedirect("/showos")
    else: #요청값에 "favorite_os"이 없는경우 
        return render(request, 'selectos.html')  #을 만나게한다.
        
def showOsFunc(request):
    #html에 전달하는게 목적이기때문에 dict type 갈게요~
    dict_context={}
    
    if "f_os" in request.session: #세션 값 중에 "f_os"가 있으면 처리
        print('유효시간: ',request.session.get_expiry_age())
        dict_context['sel_os']=request.session["f_os"] #'sel_os'키로 세션에 "f_os"를 넣어준다.
        dict_context['message']="그대가 선택한 운영체제는 %s"%request.session["f_os"]
    else:
        dict_context['sel_os']=None
        dict_context['message']="운영체제를 선택하지 않았군요"
        
    #del request.session["f_os"] #특정 세션 삭제  
    request.session.set_expiry(5) #5초동안 세션 유효
    #set_expiry(0) #브라우저가 닫힐 때 세션이 해제된다
    
    return render(request,'show.html',dict_context)
        
        