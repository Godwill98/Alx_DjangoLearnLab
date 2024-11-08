import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()
    return [book.title for book in books]

# 2. List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return [book.title for book in books]

# 3. Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    return librarian.name if librarian else "No librarian assigned"

# Testing the queries
if __name__ == "__main__":
    # Add your test data before running queries or use Django Admin to add data.
    print(get_books_by_author("J.K. Rowling"))
    print(get_books_in_library("City Library"))
    print(get_librarian_for_library("City Library"))
