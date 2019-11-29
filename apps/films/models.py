from django.db import models
from users.models import User

# Create your models here.
class Genre(models.Model):
    title = models.CharField('Genre Title', max_length = 200)

    def __str__(self):
        return self.title

class Director(models.Model):
    first_name = models.CharField('First Name', max_length = 100)
    last_name = models.CharField('Last Name', max_length = 100)
    def __str__(self):
        return self.last_name

class Actor(models.Model):
    first_name = models.CharField('First Name', max_length = 100)
    last_name = models.CharField('Last Name', max_length = 100)
    image = models.CharField('Avatar URL', max_length = 1000)
    def __str__(self):
        return self.last_name

class Film(models.Model):
    title = models.CharField('Article Title', max_length = 100)
    description = models.TextField('Article Short Description')
    image = models.CharField('Cover Image URL', max_length = 1000)
    created_at = models.DateTimeField('Publication Date')
    genres = models.ManyToManyField(Genre, null = True)
    year = models.IntegerField('Production year', default = 0)
    director = models.ForeignKey(Director, on_delete = models.CASCADE, null = True)
    duration = models.IntegerField('Film Duration', default = 0)
    actors = models.ManyToManyField(Actor, null = True)
    video = models.TextField('Film URL', default = None, null = True)
    def __str__(self):
        return self.title

class Commentary(models.Model):
    author = models.CharField('Author', max_length = 100)
    text = models.TextField('Text')
    film = models.ForeignKey(Film, on_delete = models.CASCADE)

class Rate(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    rate = models.IntegerField('Rating', default = 0)
    film = models.ForeignKey(Film, on_delete = models.CASCADE, null = True)

class Seance(models.Model):
    film = models.ForeignKey(Film, on_delete = models.CASCADE, null = True)
    price = models.IntegerField('Price', default = 1500)
    time = models.DateTimeField('Seance time')

class Book(models.Model):
    code = models.CharField('Secret Code', max_length = 100)
    email = models.CharField('Email', max_length = 100)
    seat_number = models.IntegerField('Seat number', default = 0)
    seance = models.ForeignKey(Seance, on_delete = models.CASCADE, null = True)
