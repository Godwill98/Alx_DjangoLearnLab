# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.views import generic

from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):
    queryset = Book.objects.all()  # Retrieve all Book objects
    serializer_class = BookSerializer  # Use the BookSerializer
