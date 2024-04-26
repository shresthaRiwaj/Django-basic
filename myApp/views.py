from django.shortcuts import render
# from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def home(request):
    # return HttpResponse("Hello")
    return render(request,'home.html')
def about(request):
    # return  HttpResponse("About Page")
    return render(request, "about.html")