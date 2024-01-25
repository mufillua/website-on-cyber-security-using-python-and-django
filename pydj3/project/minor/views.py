from django.shortcuts import render
from django.http import HttpResponse
from minor.models import *

# Create your views here.
def test(request):
    return HttpResponse('Testing the first page')
    
def home(request):
    return render(request,'home.html')
    
    
def kali(request):
    return render(request,'kali.html')
    
def androidguide(request):
    return render(request,'androidguide.html')
    
def linuxguide(request):
    return render(request,'linuxguide.html')
    
def windowsguide(request):
    return render(request,'windowsguide.html')
    
def spam(request):
    return render(request,'spam.html')
    
def cyberthreats(request):
    return render(request,'cyberthreats.html')
    
def aws(request):
    return render(request,'aws.html')
    
def awssecurity(request):
    return render(request,'awssecurity.html')
    
def services(request):
    return render(request,'services.html')
    
def ser(request):
    try:
        if request.method=="POST":
            u=user()
            u.fname=request.POST.get('fname')
            u.lname=request.POST.get('lname')
            u.email=request.POST.get('email')
            u.phno=request.POST.get('phno')
            u.subject=request.POST.get('subject')
            u.save()
            return render(request,'services.html')
        else:
            return render(request,'home.html')
    except:
        return render(request,'home.html')
        
        
def showcomplains(request):
    a=user.objects.all()
    return render(request,'showcomplains.html',{'a':a})
    
    
def signup(request):
    return render(request,'signup.html')
    
def sig(request):
    try:
        if request.method=="POST":
            x=user2()            
            x.email=request.POST.get('email')
            x.pwd=request.POST.get('pwd')
            x.save()
            return render(request,'signup.html')
        else:
            return render(request,'welcome.html')
    except:
        return render(request,'welcome.html')
   
   
def login(request):
    return render(request,'login.html')
    
def logcode(request):
    email=request.POST.get('email')
    pwd=request.POST.get('pwd')
    try:
        if user2.objects.filter(email=email,pwd=pwd).exists():
            return render(request,'welcome.html')
        else:
            return render(request,'login.html')
    except:
        return render(request,'login.html')
        
        
