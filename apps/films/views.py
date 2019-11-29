from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import Film, Genre, Actor, Director, Commentary, Rate, Seance, Book
from users.models import User
from django.utils import timezone
from django.db.models import Avg
from datetime import datetime
import hashlib
from random import randint

def index(request):
    films = Film.objects.all
    genres = Genre.objects.all
    return render(request, 'films/index.html', {'films': films, 'genres': genres})

def news(request):
    films = Film.objects.order_by('-id')[:10]
    genres = Genre.objects.all
    return render(request, 'films/index.html', {'films': films, 'genres': genres, 'page_title': "Новинки"})

def film(request, id=None):

    try:
        film = Film.objects.get(id=id)
        genres = Genre.objects.all
        commentaries = Commentary.objects.filter(film=film).order_by('-id')
        rating = str(Rate.objects.filter(film=film).aggregate(Avg('rate'))['rate__avg'])
        seances = Seance.objects.filter(film=film)
    except:
        raise Http404("Фильм не найден!")
    return render(request, 'films/film.html', {'film': film, 'genres': genres, 'commentaries': commentaries, 'rating': rating, 'seances': seances, 'todayDate': datetime.now().strftime("%d.%m.%Y")})

def genre(request, id=None):
    try:
        films = Film.objects.filter(genres=Genre.objects.get(id=id))
        genres = Genre.objects.all
        genre = Genre.objects.get(id=id)
    except:
        raise Http404("Жанр не найден!")
    return render(request, 'films/index.html', {'films' : films, 'genres': genres, 'page_title': "Фильмы в жанре "+genre.title})

def actor(request, id=None):
    try:
        actor = Actor.objects.get(id=id)
        films = Film.objects.filter(actors=actor)
        genres = Genre.objects.all
    except:
        raise Http404("Актер не найден!")
    return render(request, 'films/index.html', {'films' : films, 'genres': genres, 'page_title': "Фильмы в которых снялся "+actor.first_name + " "+actor.last_name})

def director(request, id=None):
    try:
        director = Director.objects.get(id=id)
        films = Film.objects.filter(director=director)
        genres = Genre.objects.all
    except:
        raise Http404("Актер не найден!")
    return render(request, 'films/index.html', {'films' : films, 'genres': genres, 'page_title': "Фильмы режиссера "+director.first_name + " "+director.last_name})

def comment(request):
    film = Film.objects.get(id=request.GET['film'])
    comment = Commentary(author=request.GET['author'], film=film, text=request.GET['text'])
    comment.save()
    return redirect('/films/'+request.GET['film'])

def rating(request):
    if request.session['auth'] != None:
        rate = request.GET['rate']
        user = User.objects.get(email=request.session['auth'])
        film = Film.objects.get(id=request.GET['film'])
        if Rate.objects.get(user=user, film=film):
            return redirect('/films/'+request.GET['film'])
        else:
            rating = Rate(user=user, rate=rate, film=film)
            rating.save()
            return redirect('/films/'+request.GET['film'])
    else:
        return redirect('/users/sign_in')

def tickets(request, id=None):
    session = Seance.objects.get(id=id)
    seats_got = list(Book.objects.filter(seance=session).values_list('seat_number', flat=True))
    return render(request, 'films/tickets.html', {'seance': session, 'film': session.film, 'seats_number': range(1,121), 'seats_got': seats_got})

def success(request, id=None):
    book = request.POST
    if Seance.objects.get(id=request.POST.get('seance')):
        seance = Seance.objects.get(id=request.POST.get('seance'))
        info = {}
        info['seats'] = ",".join(book.getlist('seat[]'))
        info['secret'] = randint(10000, 99999)
        for seat in book.getlist('seat[]'):
            se = Book(email=request.POST['email'], code=info['secret'], seat_number=seat, seance=seance)
            se.save()
        return render(request, 'films/success.html', {'book': book, 'seance': seance, 'film': seance.film, 'info': info})
    else:
        raise Http404("")
