# Create your views here.

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework import viewsets

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Retrieve all Book objects
    serializer_class = BookSerializer  # Use the BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Retrieve all Book objects
    serializer_class = BookSerializer  # Use the BookSerializer
    permission_classes = [IsAuthenticated]  # Require authentication for all requests