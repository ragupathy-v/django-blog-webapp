from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def register(request):
    if request.method=='POST':
        
        username=request.POST['username'].strip()
        email=request.POST['email'].strip()
        password=request.POST['password'].strip()

        if not( username and email and password ):
            messages.error(request,'enter a valied username and email and password')
            return redirect('register')
        else:
            if User.objects.filter(username=username).exists():
                print('username is already taken')
                messages.error(request,'username is already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print(email,'is alread exist')
                messages.error(request,'email id is already registered')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                print( 'user created' ,email,password,username)
                messages.success(request,'user created succesfully')
                return redirect('login')
        
    else:
         return render(request,'register.html')

def user_login(request):
    print(request.user)
    if request.user.is_authenticated:
        return redirect('home_page')
    if request.method=='POST':
        
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        loguser=authenticate(request,username=username,password=password)
        print(loguser)
        if loguser is not None:
            login(request,loguser)
            return redirect('home_page')
        else:
            messages.error(request,'wrong credital')
            return redirect('login')
        
    else:
        return render(request,'login.html')
    
@login_required
def user_logout(request):
    logout(request)
    return redirect('login')


