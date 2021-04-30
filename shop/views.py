from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.
def index(request):
    products = Product.objects.all()
    #print(products)
    n = len(products)
    nSlides = ceil(n/4)
    params={'no_of_slides': nSlides ,'range': range(1,nSlides) , 'product':products}
    return render(request,'shop/index.html',params) 

def about(request):
    return render(request,'shop/about.html')

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

