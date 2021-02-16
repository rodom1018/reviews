from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    # list_display = ()
    list_filter = (
        "preference",
        "favour_book",
        "favour_movie",
        "language",
    )

    fieldsets = UserAdmin.fieldsets + (
        ("Info", {"fields": ("language", "preference", "bio")}),
        ("Favour", {"fields": ("favour_book", "favour_movie")}),
    )
