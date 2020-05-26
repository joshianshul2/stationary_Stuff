from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db.models.functions import Lower
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

''' Data Structure Part :
Here We Implement a Sorting Algorithm as a filter in which we are trying  to arrange the name on basis of Their Names which is use to 
sort their Names .Here we are Use Use Quick Sort to implement in it because its faster and effective having complexity O(nlogn) .'''

def dsa(request) :

    # data = User.objects.all()
     # data = Students.objects.all()
    data1 = User.objects.order_by(Lower('name'))
    # MyModel.objects.order_by(Lower('myfield'))

    stu = {
         "dsa1": data1
         }

    return render_to_response("dsa.html", stu)


    # # print(dsa[0].name)
    # return  render(request,'dsa.html',{ 'data' : data })

