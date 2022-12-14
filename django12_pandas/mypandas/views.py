from django.shortcuts import render
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mypandas.models import Jikwon
plt.rc('font', family='malgun gothic')  #한글깨짐 방지

# Create your views here.
def mainFunc(request):
    return render(request,'main.html')

#PANDAS로 데이터 넘기기
def showFunc(request):
    jikwons=Jikwon.objects.all().values()
    #print(jikwons)
    df=pd.DataFrame.from_records(data=jikwons)
    df.columns=['사번','직원명','부서번호','직급','연봉','입사일','성별','평점']
    #print(df.head(2))
    
    #직급별 연봉합
    jik_group=df['연봉'].groupby(df['직급'])
    #jik_group2=df.groupby(df['직급'])['연봉']
    print(jik_group.sum())
    #print(jik_group2.sum())
    
    #직급별 연봉합/평균
    jik_group_detail={'sum':jik_group.sum(),'avg':jik_group.mean()}
    df2=pd.DataFrame(jik_group_detail) #DataFrame으로 넘기면 to_html()로 넘길 수 있다.
    
    #crosstab
    ctab=pd.crosstab(df['직급'],df.성별)
    #print(ctab)
    
    #시각화
    jik_result=jik_group.agg(['sum','mean'])
    #print(jik_result)
    #pandas의 Dataframe으로 시각화 지원
    jik_result.plot(kind='barh')
    plt.title('직급별 연봉 합/평균')
    plt.xlabel('연봉')
    plt.ylabel('직급')
    fig=plt.gcf() #시각화저장을 손으로한다고?
    fig.savefig('C:/work/psou/django12_pandas/mypandas/static/images/jik.png') #절대적인 주소 써야한다 성대적주소 안됨
    
    #값을 주려면 redirect로 하면 안됨 forwarding해야함
    return render(request,'list.html',
                  {'datas':df.to_html(index=False),
                   'jik_group':jik_group,
                   #'jik_group2':jik_group.to_html(), err: SeriesGroupby는 to_html로 넘길 수 없다.
                   'jik_group_detail':df2.to_html(),
                   'ctab':ctab.to_html()
                   })