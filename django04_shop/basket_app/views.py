from django.shortcuts import render

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')

def page1Func(request):
    return render(request, 'page1.html')

def page2Func(request):
    return render(request, 'page2.html')

def cartFunc(request):
    name=request.POST["name"]
    price=request.POST["price"]
    product = {'name':name, 'price':price} #클라이언트가 넘겨주는거 때거지로 받을 때 자바의 폼빈같은거 dto는 db랑 왔다갔다 같은거
    
    productList=[] #상품통
    
    #shop이라는 키로다가 productList를 담은것
    if "shop" in request.session:  #session에 shop이라는 키의 통
        productList=request.session["shop"] #session 내에 shop이라는 key로 productList가 등록
        productList.append(product)
        request.session["shop"]=productList
    else:
        productList.append(product) #제일 첫번째 상품은 여기로 온다(왜냐면 shop이 없을테니까)
        request.session["shop"]=productList
    
    print(productList)
    context={}
    #products라는 키로다가 shop에 있는 값을 담는다.
    context['products']=request.session['shop']
    #context에는 products 가 들어있다 #이건 여러개가 담겨있으니 반복문을 돌려서 빼낸다. 자 cart.html로 가즈아
    return render(request, 'cart.html',context)
        
def buyFunc(request):
    if "shop" in request.session:
        productList=request.session["shop"]
        total=0
        
        for p in productList:
            total+=int(p['price'])
        
        print('결제총액: ',total)
        request.session.clear() #세션 내의 모든 키 삭제
        #del request.session['shop'] #특정 키를 가진 세션 내용 삭제

    return render(request, 'buy.html',{'total':total})
