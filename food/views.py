from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import *
from .forms import *
# Create your views here.
def test(request):
    return HttpResponse('testing the page')

def home(request):
    return render(request,'home.html')

def second(request):
    return render(request,'second.html')

def third(request):
    return render(request,'third.html')

def forth(request):
    return render(request,'forth.html')
def demo(request):
    return render(request,'demoproject.html')
def form(request):
    return render(request,'form.html')
def insert(request):
    try:
        if request.method=='POST':
            x=user()
            x.username=request.POST.get('uname')
            x.email=request.POST.get('email')
            x.password=request.POST.get('pwd')
            x.save()
            return render(request,'form.html')
        else:
            return render(request,'form.html')
    except Exception as e:
        return HttpResponse(e)

def customer1(request):
    return render(request,'customer.html')

def ins(request):
    try:
        if request.method=='POST':
            x=customer()
            x.name=request.POST.get('name')
            x.phone=request.POST.get('phone')
            x.email=request.POST.get('email')
            x.address=request.POST.get('add')
            x.save()
            return render(request,'customer.html')
        else:
            return render(request,'customer.html')
    except Exception as e:
        return HttpResponse(e)

def display(request):
    x=customer.objects.all()
    return render(request,'display.html',{'a':x})
def dele(request,id):
    u=customer.objects.get(id=id)
    u.delete()
    return redirect('../display')
def edit(request,id):
    c=customer.objects.get(id=id)
    return render(request,'edit.html',{'c':c})
def edcode(request,id):
    try:
        t=customer.objects.get(id=id)
        form=cform(request.GET,instance=t)
        if form.is_valid():
            form.save()
            return redirect('../display')
        return render(request,'edit.html',{'c':t})
    except Exception as e:
        return HttpResponse(e)
    
    



    