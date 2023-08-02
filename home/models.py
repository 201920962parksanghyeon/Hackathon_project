from django.db import models

class Post(models.Model): #메인화면 포스트 모델
    title = models.CharField(max_length=30) #제목
    content = models.TextField() #내용
    created_at = models.DateTimeField() #작성일


    def __str__(self): #포스트 제목, 번호 보여주기
       return f'[{self.pk}]{self.title}'
# Creat e your models here.
