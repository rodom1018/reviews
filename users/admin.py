from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("user_name",)
    list_filter = (
        "preference",
        "favour_book",
        "favour_movie",
        "language",
    )

    fieldsets = (
        ("Info", {"fields": ("user_name", "language", "preference", "bio")}),
        ("Favour", {"fields": ("favour_book", "favour_movie")}),
    )
