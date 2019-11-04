from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id>/', views.film, name="film"),
    path('news/', views.news, name="news"),
    path('rating/', views.rating, name="rating")
]
