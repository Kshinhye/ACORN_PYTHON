from django.shortcuts import render
from sangpum.models import Maker, Product

# Create your views here.
def Main(request):
    return render(request,'main.html')

def List1(request):
    makers=Maker.objects.all()
    return render(request, 'list1.html',{'makers':makers})

def List2(request):
    products=Product.objects.all()
    pcount=len(products)
    return render(request, 'list2.html',{'products':products,'pcount':pcount})

def List3(request): #id를 받아야한다.
    mid=request.GET.get("id") #id에 해당되는 자료만 나와주면 된다~
    products=Product.objects.filter(make_name=mid) #filter: sql문 where문 생각
    pcount=len(products)
    return render(request, 'list2.html',{'products':products,'pcount':pcount})
