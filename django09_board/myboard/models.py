from django.db import models

# Create your models here.
class BoardTab(models.Model):

    name = models.CharField(max_length = 20)
    passwd = models.CharField(max_length = 20)
    mail = models.CharField(max_length = 30)
    title = models.CharField(max_length = 100)
    cont = models.TextField()
    bip = models.GenericIPAddressField()
    bdate = models.DateTimeField()
    readcnt = models.IntegerField()
    gnum = models.IntegerField() #그룹넘버
    onum = models.IntegerField() #그룹내 댓글넘버
    nested = models.IntegerField() #들여쓰기