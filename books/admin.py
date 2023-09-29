from django.contrib import admin
from .models import Book, Genre

@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Genre)
class GenreModelAdmin(admin.ModelAdmin):
    pass

# Register your models here.
