from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    genre = serializers.StringRelatedField(many=True)
    class Meta:
        model = Book
        fields = '__all__'