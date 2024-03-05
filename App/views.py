from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

def index(request):
    return render(request,"index.html")
def main(request):
    return render(request,"main.html")

def http(request):
    return render(request,"http1.html")

def cat(request):
    return render(request,"www2.html")

def md(request):
    return render(request,"module3.html")

def dj(request):
    return render(request,"djcomment4.html")

def tm(request):
    return render(request,"templates5.html")
