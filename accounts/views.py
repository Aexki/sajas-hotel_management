from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import cabservice,roomservice,complaintservice

# Create your views here.

def preference(request):
    return render(request, 'preference.html')

def food(request):
    return render(request, 'food.html')

def business_feature(request):
    if request.method=='POST':
        n="Aexki"
        s=request.POST.get('feature')
        
        user=roomservice(name=n, service=s)
        user.save()
    return render(request, 'business_feature.html')

def feature(request):
    if request.method=='POST':
        n="Aexki"
        s=request.POST.get('feature')
        
        user=roomservice(name=n, service=s)
        user.save()
    return render(request, 'feature.html')

def thanku(request):
    if request.method=='POST':
        n=request.POST.get('username')
        r=request.POST.get('room')
        c=request.POST.get('complaint')
        
        user=complaintservice(name=n, room=r, complaint=c)
        user.save()
        
    return render(request, 'feature.html')

def bthanku(request):
    if request.method=='POST':
        n=request.POST.get('username')
        r=request.POST.get('room')
        c=request.POST.get('complaint')
        
        user=complaintservice(name=n, room=r, complaint=c)
        user.save()
        
    return render(request, 'business_feature.html')
    

    
def cab(request):
    if request.method=='POST':
        n="Aexki"
        p=request.POST.get('package')
        d=request.POST.get('date')
        
        user=cabservice(name=n,package=p,date=d)
        user.save()
           
    return render(request, 'cab.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("./preference")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        phone = request.POST['phone']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Another User exists with the same username')
                return redirect('register')
            
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Account with the given email id already exists, Try login in')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'Password does not match')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
