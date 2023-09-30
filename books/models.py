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

    
    def __str__(self):
        return self.genre_name
    

class Book(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='book_author')
    title = models.CharField(max_length=50, unique=True)
    genre = models.ManyToManyField(Genre)
    condition = models.CharField(choices=BOOK_CONDITIONS, default='new', max_length=20)
    description = models.TextField(max_length=255)
    available = models.BooleanField(default=True)
    recipient = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True, related_name='recipient')
    location = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        db_table = "book"
    
    def author_full_name(self):
        return f'{self.author.first_name} {self.author.last_name}'
    
    def __str__(self):
        return self.title