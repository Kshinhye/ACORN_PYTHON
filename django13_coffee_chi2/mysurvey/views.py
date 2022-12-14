from django.shortcuts import render, redirect
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
plt.rc('font',family='malgun gothic')
from mysurvey.models import Survey

# Create your views here.
def surveyMain(request):
    return render(request,'main.html')

def surveyView(request):
    return render(request,'survey.html')

def surveyProcess(request):
    #함수를 따로 만들어볼게요 #설문조사 결과를 DB에 저장
    insertData(request)
    return redirect("/coffee/surveyshow") #insert 후 분석결과보기

def surveyAnalysis(request):
    #데이터 읽어오기
    rdata=list(Survey.objects.all().values())
    #objects까지하면 queryset type 그래서 values를 읽어와 list에 담아준다.
    #print(rdata)
    df=pd.DataFrame(rdata)
    df.dropna()
    #print(df)
    
    ctab=pd.crosstab(index=df['gender'],columns=df['co_survey'])
    ctab.index=['남','여']
    ctab.columns=['스타벅스','이디야','커피빈','탐앤탐스']
    #print(ctab)
    
    #카이스퀘어 추정 및 검정
    chi, pv,_,_=stats.chi2_contingency(observed=ctab)
    print('chi: {}, pv: {}'.format(chi,pv))
    
    if pv>0.05:
        result="<h3>P값(유의확률)이 {} > 0.05(유의수준)이므로 <br> 성별과 커피브랜드의 선호도는 관계가 없다.<br> <mark>귀무가설 채택</mark></h3>".format(pv)
    else:
        result="<h3>P값(유의확률)이 {} < 0.05(유의수준)이므로 <br> 성별과 커피브랜드의 선호도는 관계가 있다.<br> <mark>대립가설 채택</mark></h3>".format(pv)
    
    count=len(df)
    
    #시각화: 커피 브랜드별
    fig=plt.gcf()
    coffee_group=df.groupby(['co_survey'])['rnum'].count()
    coffee_group.plot.bar(subplots=True, color=['green','blue','gray','red'], width=0.5, rot=0)
    plt.xlabel('커피브랜드명')
    plt.title('커피 브랜드별 선호 건수')
    plt.grid()
    fig.savefig('django13_coffee_chi2/mysurvey/static/images/coffee.png')

    return render(request, 'list.html',{'ctab':ctab.to_html(), 'result':result, 'count':count})
    
def insertData(request): #설문조사 결과를 DB에 저장
    #print(request.POST.get('gender'),'',request.POST.get('age'),'',request.POST.get('co_survey'),'',)
    if request.method=="POST":
        Survey(
            gender=request.POST.get('gender'),
            age=request.POST.get('age'),
            co_survey=request.POST.get('co_survey')
        ).save()
        
    #else 어쩌구 저쩌구는 그냥 다 생략한다.