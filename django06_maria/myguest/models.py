from django.db import models

# Create your models here.
class Guest(models.Model):
    #myno=models.AutoField(Auto_created=True, primary_key=True) #이러면 id가안생기고 얘가 생긴다. 주석처리하면 id가 생긴다
    title=models.CharField(max_length=50)
    content=models.TextField()
    regdate=models.DateTimeField()
    
    #내부클래스(정렬)
    class Meta:
        # ordering=('title',)  #ordering은 튜플로 줘야한다.
        # ordering=('-title','id')
        ordering=('-id',)