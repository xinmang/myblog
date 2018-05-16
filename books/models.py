from django.db import models

# Create your models here.
class Publisher(models.Model):
     publisher_name = models.CharField(max_length=30)
     address = models.CharField(max_length=50)
     city = models.CharField(max_length=60)
     province = models.CharField(max_length=30)
     country = models.CharField(max_length=50)
     website = models.URLField()

     class Meta:
          ordering = ('publisher_name',)     

     def __str__(self):
          return self.publisher_name

class Auther(models.Model):
     SEX = (
          ('M','Male'),
          ('F','Female'),
          )
     first_name = models.CharField(max_length=30)
     last_name = models.CharField(max_length=30)
     email_address = models.EmailField()
     age = models.IntegerField()
     sex = models.CharField(max_length=1,choices=SEX)

     def __str__(self):
          return '%s %s'%(self.first_name,self.last_name)

class Book(models.Model):
     name = models.CharField(max_length=100)
     pagenum = models.IntegerField()
     price = models.DecimalField(max_digits=10,decimal_places=2)
     auther = models.ManyToManyField(Auther)
     publisher_name = models.ForeignKey(Publisher)
     publication_time = models.DateField()

     def __str__(self):
          return self.name
