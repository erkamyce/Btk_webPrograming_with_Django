from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('anasayfa', views.home),
    path('<kurs_detay>', views.course),
    path('kategori/<int:category_id>', views.getcoursesByCategoryId),
    path('kategori/<str:category_name>', views.getcoursesByCategory),
]