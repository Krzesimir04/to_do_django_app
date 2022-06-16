from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import CharField, Form,PasswordInput

class NewUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'email', 'password1','password2']

class LoginForm(Form):
    username=CharField(max_length=100)
    password=CharField(widget=PasswordInput(),max_length=555)