from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Task(models.Model):
    header=models.CharField(max_length=50)
    describtion=models.TextField(null=True)
    end_date=models.DateTimeField(null=True)
    category=models.ForeignKey(Category,null=True,on_delete=models.CASCADE,blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    def __str__(self):
        return self.header

