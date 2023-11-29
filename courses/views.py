from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import  reverse

data ={
    "programlama":"Programlama kategorisine ait kurslar",
    "mobil":"mobil kategorisine ait kurslar",
    "web-gelistirme":"web-gelistirme kategorisine ait kurslar",
}
# Create your views here.

# deneme commit
def index (request):
    return render(request,'index.html')

def about (request):
    return render(request,'about.html')

def contact (request):
    return render(request,'contact.html')