from datetime import datetime
from django.shortcuts import redirect, render
from .models import *
from .forms import NewUserForm,LoginForm,NewTaskForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    #check if user is login and show his tasks.
    if  request.user in User.objects.all():
        tasks=Task.objects.filter(user=request.user)
        if tasks.exists():
            return render(request,'index.html',{'tasks':tasks})
        else:
            return render(request,'index.html')
    else:
        return render(request,'index.html')


def register(request):
    if request.method == 'POST':
        form=NewUserForm(request.POST)
        username=request.POST['username']
        if User.objects.filter(username=username).exists():
            messages.info(request,'there already is user with this name, please change your username')
            return redirect('register')
        email=request.POST['email']
        if User.objects.filter(email=email).exists():
            messages.info(request,'there already is user with this email, please change your email')
            return redirect('register')
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1!=password2:
            messages.info(request,'passwords are not the same')
            return redirect('register')
        form.save()
        messages.success(request,'Account Created')
        return redirect('login')
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

@login_required(login_url='login')
def new(request):
    if request.method=='POST':
        form=NewTaskForm(request.POST)

        header=request.POST['header']
        describtion=request.POST['describtion']
        end_date=request.POST['end_date']
        category_number=request.POST['category']

#if category is None then don't set this option
        if category_number != '':
            category=Category.objects.get(id=category_number)
            newTask=Task(header=header,category=category,describtion=describtion,end_date=end_date,user=request.user)
        else:
            newTask=Task(header=header,describtion=describtion,end_date=end_date,user=request.user)

        newTask.save()
        return redirect('index')
    else:
        form=NewTaskForm()
    return render(request, 'new.html',{'form':form})

@login_required(login_url='login')
def delete(request,pk):
    Task.objects.filter(id=pk,user=request.user).delete()
    return redirect('index')

@login_required(login_url='login')
def edit(request,pk):
    if request.method=='POST':
        task=Task.objects.filter(id=pk,user=request.user)
        EditForm=NewTaskForm(request.POST)

        if EditForm.is_valid():
            header=request.POST['header']
            describtion=request.POST['describtion']
            end_date=request.POST['end_date']
            category_number=request.POST['category']
#validate category and end_date(validator)
            if category_number != '':
                category=Category.objects.get(id=category_number)
                validator(request,end_date,task,header,category,describtion)
            else:
                validator(request,end_date,task,header,None,describtion)
            return redirect('index')

        else:
            task=Task.objects.get(id=pk,user=request.user)
            EditForm=NewTaskForm(initial=[{'header':task.header,'describtion':task.describtion,'end_date':task.end_date,'category':task.category}])
            return render(request,'edit.html',{'form':EditForm})

#sending user a form with full data about task to edit it
    elif request.method=='GET':
        task=Task.objects.get(id=pk,user=request.user)
        EditForm=NewTaskForm(initial={'header':task.header,'describtion':task.describtion,'end_date':task.end_date,'category':task.category})
        return render(request,'edit.html',{'form':EditForm})
    return redirect('index')


#checking end_date
def validator(request,end_date,task,header,category,describtion):
    if end_date == '' or end_date<str(datetime.now().date()):
        task.update(header=header,category=category,describtion=describtion,end_date=datetime.now().date(),user=request.user)
    else:
        task.update(header=header,category=category,describtion=describtion,end_date=end_date,user=request.user)