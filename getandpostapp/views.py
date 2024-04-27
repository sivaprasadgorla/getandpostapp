from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"input.html")
def add(request):
    if request.method=="GET":
        x=int(request.GET['t1'])
        y=int(request.GET['t2'])
        z=x+y
        return HttpResponse("the sum is :"+str(z))
    else:
        x=int(request.POST['t1'])
        y=int(request.POST['t2'])
        z=x+y
        return HttpResponse("the sum is :" + str(z))



