from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'shop/index.html')

def about(request):
    return HttpResponse("About")

def contact(request):
    return HttpResponse("Contact")

def track(request):
    return HttpResponse("Tracker")

def search(request):
    return HttpResponse("Search")

def productview(request):
    return HttpResponse("Product View") 

def checkout(request):
    return HttpResponse("Checkout")

