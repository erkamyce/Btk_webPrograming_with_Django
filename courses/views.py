from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

data ={
    "programlama":"Programlama kategorisine ait kurslar",
    "mobil":"mobil kategorisine ait kurslar",
    "web-gelistirme":"web-gelistirme kategorisine ait kurslar",
}
# Create your views here.

# deneme commit
def home (request):
    return HttpResponse('Anasayfa')
def course (request, kurs_detay):
    return HttpResponse(f"{kurs_detay} detay sayfasi")

def getcoursesByCategory(request , category_name ):
    try:
        category_text = data[category_name]
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("wrong catagory ")

def getcoursesByCategoryId (request , category_id ):
    category_list = list(data.keys())
    if(category_id > len(category_list)):
        return HttpResponseNotFound("WRONG CATAGORY")
    redirect_text = category_list[category_id - 1]

    return redirect('/kurslar/kategori/' + redirect_text)