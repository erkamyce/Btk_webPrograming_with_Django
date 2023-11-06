from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# deneme commit
def home (request):
    return HttpResponse('Anasayfa')
def course (request):
    return HttpResponse('Kurs Listeleri')
