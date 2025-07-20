from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # One Author → Many Books

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)  # Many Publishers ↔ Many Books

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # One user → One profile
    bio = models.TextField()
