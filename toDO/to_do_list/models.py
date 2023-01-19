from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    header=models.CharField(max_length=50)
    describtion=models.TextField(null=True)
    end_date=models.DateField(null=True)
    category=models.ForeignKey(Category,null=True,on_delete=models.CASCADE,)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.end_date)

