from django.shortcuts import redirect, render
from .forms import NewUserForm,LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    return render(request,'index.html')


def register(request):
    if request.method == 'POST':
        form=NewUserForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get('emal')
            if User.objects.filter(email=email) is not None:
                messages.info(request,'there already is user with this email, please change your email')
                return redirect('register')
            form.save()
            messages.success(request,'Account Created')
            return redirect('login')
        else:
            username=form.cleaned_data.get('username')
            if User.objects.filter(username=username) is not None:
                messages.info(request,'there already is user with this name, please change your username')
                return redirect('register')
            
            messages.info(request,'passwords are not the same')
            return redirect('register')
    else:
        form=NewUserForm()
    return render(request, 'register.html',{'form':form})


def loginFunction(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request,'Username or password doesn\' t match')
    else:
        form=LoginForm()
    return render(request, 'login.html',{'form':form})


def logoutFunction(request):
    logout(request)
    return redirect('login')