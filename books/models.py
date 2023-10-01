from django.db import models
from accounts.models import Account


BOOK_CONDITIONS = [
    ('new', 'New'),
    ('fine', 'Fine'),
    ('very_good', 'Very Good'),
    ('good', 'Good'),
    ('fair', 'Fair'),
    ('poor', 'Poor')
]

class Genre(models.Model):
    genre_name = models.CharField(max_length=30)
    
    class Meta:
        db_table = "genre"
        ordering = ['genre_name']

    def __str__(self):
        return self.genre_name
    

class Author(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='author')
    about = models.TextField(max_length=255)
    
    def full_name(self):
        return f"{self.author.first_name} {self.author.last_name}"
    
    def __str__(self):
        return self.author.email
        
    class Meta:
        db_table = "author"


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book_author')
    title = models.CharField(max_length=50, unique=True)
    genre = models.ManyToManyField(Genre)
    condition = models.CharField(choices=BOOK_CONDITIONS, default='new', max_length=20)
    description = models.TextField(max_length=255)
    available = models.BooleanField(default=True)
    recipient = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True, related_name='recipient')
    location = models.CharField(max_length=40, blank=True, null=True)
    is_interested = models.ManyToManyField(Account, related_name="is_interested", blank=True)

    class Meta:
        db_table = "book"
        ordering = ['-id']
    
    def __str__(self):
        return self.title
    

class Images(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_image')
    image = models.ImageField(upload_to='book_image')
    
    class Meta:
        db_table = "image"
    
    def __str__(self):
        return self.image.url