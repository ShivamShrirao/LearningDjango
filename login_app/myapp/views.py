from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
	return render(request,"myapp/hello.html",{})

def base(request):
	return render(request,"myapp/base.html",{})