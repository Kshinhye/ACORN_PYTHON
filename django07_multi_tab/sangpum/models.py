from django.db import models

# Create your models here.
class Maker(models.Model):
    #id가 존재함
    mname=models.CharField(max_length=10)
    tel=models.CharField(max_length=30)
    addr=models.CharField(max_length=50)
    
    #튜플이므로 단수면 꼭 , 붙이기
    class Meta:
        ordering=('-id',)
    
    #외부키랑 관련있다
    #admin에서 설명할 예정
    #admin창을 사용하지 않을꺼면 안써도 된다
    def __str__(self):
        return self.mname
    
class Product(models.Model):
    pname=models.CharField(max_length=10)
    price=models.IntegerField()
    #외부키 만들기
    make_name=models.ForeignKey(Maker, on_delete=models.CASCADE) 
    #자동으로 Maker의 id와 맵핑된다
    #fk의 대상은 pk이므로 자동으로 ()에 입력한 class의 pk와 맵핑된다
    #CASCADE? Maker의 특정 레코드를 지우면 해당 레코드와 관련있는 Product 레코드도 같이 지워진다
    
    
        
        