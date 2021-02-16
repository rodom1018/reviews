from django.db import models
from django_countries.fields import CountryField

# Create your models here.
class User(models.Model):

    MOVIE = "movie"
    BOOK = "books"

    PREFERENCE_CHOICES = (
        (MOVIE, "Movie"),
        (BOOK, "Book"),
    )

    MALE = "male"
    FEMALE = "female"

    GENDER_CHOICES = (
        (MALE, "male"),
        (FEMALE, "female"),
    )

    user_name = models.CharField(max_length=30, blank=True)
    favour_book = models.CharField(max_length=30)
    favour_movie = models.CharField(max_length=30)
    language = CountryField()
    preference = models.CharField(max_length=20, choices=PREFERENCE_CHOICES)
    bio = models.CharField(max_length=20, choices=GENDER_CHOICES)
