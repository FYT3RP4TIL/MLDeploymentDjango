# Create your views here.
# Django MVT - Model(Database) View(Logic) Template(Html/FrontEnd)
# MVC - Model(Database) View(Logic) Controller - Java

from django.shortcuts import render
from django.http import HttpResponse

def Welcome(request):
    #return HttpResponse("<h1>Welcome to Django ML Deployment Application</h1>")
    return render(request,'index.html')

def user(request):
    username = request.GET['username'] 
    return render(request,'user.html',{'name':username}) # passing username to user.html (redirecting)