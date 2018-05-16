from django.db import models

# Create your models here.
class Post(models.Model):
     title = models.CharField(max_length=200) #文章标题
     slug = models.CharField(max_length=200) #文章网址
     body = models.TextField() #文章内容
     pub_date = models.DateTimeField('date blogs') #发表时间

     class Meta:
          ordering = ('-pub_date',)

     def __str__(self):
          return self.title #文章标题为显示内容
