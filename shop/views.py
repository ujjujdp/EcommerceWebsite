from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact
from math import ceil
# Create your views here.
def index(request):
    # products = Product.objects.all()
    #print(products)
    # n = len(products)
    # nSlides = ceil(n/4)
    # params={'no_of_slides': nSlides ,'range': range(1,nSlides) , 'product':products}
    # allProds = [
    #             [products,range(1,nSlides),nSlides],
    #             [products,range(1,nSlides),nSlides]
    #         ]
    allProds = []
    catprods = Product.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = ceil(n/4)
        allProds.append([prod,range(1, nSlides),nSlides]) 
    params = {'allProds':allProds}
    return render(request,'shop/index.html',params) 

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    if request.method=="POST":
        print(request)

    name = request.POST.get('name','')
    email = request.POST.get('email','')
    phno = request.POST.get('phno','')
    descr = request.POST.get('descr','')
    print(name)
    print(email)
    print(phno)
    print(descr)
    contact = Contact(user_name = name, email = email, phno=phno, descr = descr)
    contact.save()
    return render(request,'shop/contact.html')

def track(request):
    return render(request,'shop/tracker.html')

def search(request):
    return render(request,'shop/search.html')

def prodview(request , myid):
    # Fetch the product using ID
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request,'shop/prodview.html',{'product':product[0]})

def checkout(request):
    return render(request,'shop/checkout.html')
