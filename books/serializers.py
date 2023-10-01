from rest_framework import serializers
from .models import Book, Genre, Author, Images

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    class Meta:
        model = Author
        fields = ['id','author', 'about']
        
    def get_author(self, obj):
        return f"{obj.author.first_name} {obj.author.last_name}"
        
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['id', 'image']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    genre = GenreSerializer(many=True)
    images = serializers.SerializerMethodField()
    
    class Meta:
        model = Book
        fields  = ['id', 'title','author','images', 'genre', 'condition', 'description', 'available', 'location']
        
    def get_images(self, book):
       return ImageSerializer(book.book_image.all(), many=True).data
