from django.shortcuts import redirect, render
from .forms import NewUserForm,LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request,'index.html')


def register(request):
    if request.method == 'POST':
        form=NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account Created')
            return redirect('login')
        else:
            messages.info(request,'Something is not OK')
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