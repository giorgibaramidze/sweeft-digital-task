from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    genre = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Book
        exclude  = ['recipient']
        
    def get_author(self, obj):
        return f'{obj.author.first_name} {obj.author.last_name}'