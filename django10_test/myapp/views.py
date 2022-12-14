from django.shortcuts import render
from myapp.models import Gogek, Buser, Jikwon
import datetime

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')

def damdangFunc(request):
    if request.method == "POST":
        name=request.POST.get('name')
        tel=request.POST.get('tel')
        try:
            if Gogek.objects.get(gogek_tel=tel): #넘어온 고객 번호가 고객테이블에 있으면
                #테이블 join (FK 있어야 가능)
                jdata=Gogek.objects.select_related('gogek_damsano').get(gogek_name=name)
                
                #근로년
                day=datetime.date.today() - jdata.gogek_damsano.jikwon_ibsail
                year= day.days // 365
                
                jrating =''
                if jdata.gogek_damsano.jikwon_rating == 'a':
                    jrating +='최우수';
                elif jdata.gogek_damsano.jikwon_rating == 'b':
                    jrating +='우수';
                elif jdata.gogek_damsano.jikwon_rating == 'c':
                    jrating +='일반';
                print(jrating)
                
                #직원테이블의 부서 번호로 부서테이블의 부서번호를 찾아서 row하나를 빼낸다...?(다시 체크)
                bno=Buser.objects.get(buser_no=jdata.gogek_damsano.buser_num)
                
                datas={'dk_data':jdata.gogek_damsano, 'bno':bno ,'year':year, 'jrating':jrating}
               
        except Exception as e:
            return render(request, 'main.html', {'msg':'전화번호 또는 이름 불일치'})
            #print('damdangFunc',e) #다시 풀어보기
        return render(request, 'list.html',datas )
