from django.shortcuts import render
import pandas as pd
import pickle
# Create your views here.

df=pd.read_csv("https://raw.githubusercontent.com/pykwon/python/master/testdata_utf8/patient.csv")
df2=df[:8]
df_x=df.loc[:,['AGE','SEX','RACE','SER','CAN','INF','CPR','HRA']]
df_y=df.loc[:,'STA']

def MainFunc(request):
    model=pickle.load(open('C:/work/psou/pro1/pack10anal04/patient_model.sav','rb'))
    model_acc=model.score(df_x,df_y)
    del model
    return render(request,'main.html',{'df2':df2.to_html(),'model_acc':model_acc})

def listFunc(request):
    model=pickle.load(open('C:/work/psou/pro1/pack10anal04/patient_model.sav','rb'))
    if request.method=="POST":
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        race = request.POST.get('race')
        ser = request.POST.get('ser')
        can = request.POST.get('can')
        inf = request.POST.get('inf')
        cpr = request.POST.get('cpr')
        hra = request.POST.get('hra')
        
        data = { age:[age],
                sex:[sex],
                race:[race],
                ser:[ser],
                can:[can],
                inf:[inf],
                cpr:[cpr],
                hra:[hra]
            }
        
        test_x = pd.DataFrame(data, columns=[age, sex, race, ser, can, inf, cpr, hra])
        pred = model.predict(test_x)
    del model
    return render(request, 'list.html', {'pred':pred[0]})

def showFunc(request):
    return render(request, 'show.html')
