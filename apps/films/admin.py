from django.contrib import admin
from .models import Genre, Director, Actor, Film, Commentary, Rate, Seance, Book

# Register your models here.
admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Film)
admin.site.register(Commentary)
admin.site.register(Rate)
admin.site.register(Seance)
admin.site.register(Book)
