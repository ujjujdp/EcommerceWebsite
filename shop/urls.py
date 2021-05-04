from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="shophome"),
    path('about/', views.about, name="AboutUs"),
    path('contact/', views.contact, name="ContactUs"),
    path('tracker/', views.track, name="TrackingStatus"),
    path('search/', views.search, name="Search"),
    path('prodview/<int:myid>', views.prodview, name="ProductView"),
    path('checkout/', views.checkout, name="Checkout"),
]
