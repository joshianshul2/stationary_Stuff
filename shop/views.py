from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.
def index(request):
    if request.method == 'POST' :
        name1=request.POST['name']
        email1 = request.POST['email']
        subject1 = request.POST['subject']
        message1 = request.POST['message']
        anji=User(name=name1,email=email1,subject=subject1,message=message1)
        anji.save()

    return render(request,'index.html')


def cart(request):
    return render(request,"cart.html")
