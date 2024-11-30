from rest_framework import serializers
from .models import Book,Author
from datetime import date

"""
BookSerializer:
- Serializes all fields of the Book model.
- Includes custom validation to ensure that the publication year is not in the future.

AuthorSerializer:
- Serializes the 'name' field from the Author model.
- Dynamically includes related books using a nested BookSerializer. 
  The relationship is handled via the `source='book_set'` parameter, which fetches the reverse relation of the ForeignKey.
"""

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

      # Custom validation for publication_year
    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True, source='book_set')  # Nested serializer for related books

    class Meta:
        model = Author
        fields = ['name', 'books']