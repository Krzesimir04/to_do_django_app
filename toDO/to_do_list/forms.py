from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Category
from django.forms import CharField, Form,PasswordInput,ModelChoiceField,Textarea,DateTimeField,DateTimeInput

#widget for end_date in NewTaslForm
class MyDateInput(DateTimeInput):
    input_type='datetime-local'

class NewUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'email', 'password1','password2']

class LoginForm(Form):
    username=CharField(max_length=100)
    password=CharField(widget=PasswordInput(),max_length=555)

class NewTaskForm(Form):
    header=CharField(max_length=50)
    category=ModelChoiceField(queryset=Category.objects.all(),empty_label='None',required=False)
    describtion=CharField(widget=Textarea,required=False)
    end_date=DateTimeField(label='Date to end',widget=MyDateInput,required=False,initial=datetime.now)