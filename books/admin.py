from django.contrib import admin
from .models import Book, Genre, Author, Images

class ImagesInline(admin.TabularInline):
    model = Images
    extra = 1

@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    inlines = [ImagesInline]

@admin.register(Genre)
class GenreModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    pass


# Register your models here.
