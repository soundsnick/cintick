from django.db import models

class User(models.Model):
    email = models.CharField('Email', max_length = 100)
    password = models.CharField('Password', max_length = 100)
    def __str__(self):
        return self.email
