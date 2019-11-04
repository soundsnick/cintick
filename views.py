from django.http import HttpResponse
from django.shortcuts import render
from .models import Genre

def index(request):
    genres = Genre.object.all
    return render(request, 'films/index.html', {'genres': genres})
