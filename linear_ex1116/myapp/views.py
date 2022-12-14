from django.shortcuts import render
from myapp.models import Jikwon
from django.http.response import HttpResponse, JsonResponse
import datetime
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import json

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def ListFunc(request):
    return render(request, 'list.html')

def ListDbFunc(request):
    #이렇게하면 이 요청을 받을 때 마다 데이터를 읽어오고,
    #학습을 하기때문에 따로 함수로 만들어놓거나 모델을 저장해두고 부르는게 좋아요
    #모델저장은 꼭 장고에서 안해도 돼요, 그다음 if문으로 있으면 만들지말고 없으면 만들어 이런식으로!
    
    jikwons=Jikwon.objects.all().values()
    df1=pd.DataFrame.from_records(data=jikwons)
    
    pay=[]
    for p in jikwons:
        pay.append(p['jikwon_pay'])
    #print(pay)
    
    ibsail=[]
    for i in jikwons:
        year=(datetime.date.today()-i['jikwon_ibsail']).days // 365
        ibsail.append(year)
    #print(ibsail)
    
    df2=pd.DataFrame(pay,columns=['연봉'])
    df2['근무년수']=ibsail
    
    x=df2[['근무년수']].values
    y=df2['연봉'].values
    
    model=LinearRegression().fit(x,y)
    #model.coef_ : [570.0937012]
    #model.intercept_: 649.2347735554404
    
    pred=model.predict(x)
    # print('예측값: ',pred[:5])
    # print('실제값: ',y[:5])
    rscore=int(r2_score(y,pred)*100)
    
    # 추가적으로 모델을 확인할 수 있는 메뉴도 추가해주면 좋아요(ex.모델 정보 알아보기)

    #근무년수에 대한 연봉을 이용하여 회귀분석 모델을 작성
    #장고로 작성한 웹에서 근무년수를 입력하면 예상 연봉이 나올 수 있도록 프로그래밍
    if request.method=="POST":
        year=int(request.POST.get('year'))
        #print(year)
        new_x=[[year]]
        new_pred=model.predict(new_x)[0].round()
        #print(new_pred) #<class 'numpy.ndarray'>
    
    
    #직급별 연봉 평균
    javg=df1['jikwon_pay'].groupby(df1['jikwon_jik']).mean().round()
    djavg=pd.DataFrame(javg)
    djavg.columns=['평균 연봉']
    
    return JsonResponse({'new_pred':new_pred,'rscore':rscore,'javg':djavg.to_html()})