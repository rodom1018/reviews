from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    
    KOR = "Korean"
    ENG = "English"

    LANGUGAGE_CHOICES = (
        (KOR, "Korean"),
        (ENG, "English"),
    )
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

    favour_book = models.CharField(max_length=30, blank=True)
    favour_movie = models.CharField(max_length=30, blank=True)
    language = models.CharField(max_length=20, choices=LANGUGAGE_CHOICES, blank=True)
    preference = models.CharField(max_length=20, choices=PREFERENCE_CHOICES, blank=True)
    bio = models.TextField(default="")
    