from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == "POST":
        login_email=request.POST['loginemail']
        login_pass1=request.POST['loginpass1']
        
        user = authenticate(username=login_email,password=login_pass1)

        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged In")
            return redirect('index1')
        else:
            # messages.error(request,"Invalid , Please try again")
            return redirect('home')
    return render(request,"FullLoginSingupPage/login.html")
def sing_up(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if pass1!=pass2:
            return HttpResponse('Your password & Conform Password are not same')
        else:
            data = User.objects.create_user(username=name,email=email,password=pass1)
            data.save()
            messages.success(request,"Account has been successfully created")
            return redirect('login')
        
    return render(request,"FullLoginSingupPage/singup.html")
    

def home(request):
    return render(request,"FullLoginSingupPage/index.html")

def log_out(request):
    logout(request)
    messages.success(request, "Profile details updated.") 
    return redirect('home') 

    # return HttpResponse('logout')

def index1(request):
    return render(request,"FullLoginSingupPage/index1.html")