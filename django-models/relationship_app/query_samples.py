import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author using `filter()`
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)  # Using filter() here
        return [book.title for book in books]
    except Author.DoesNotExist:
        return f"Author '{author_name}' not found."

# 2. List all books in a library using `filter()`
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = Book.objects.filter(libraries=library)  # Using filter() here with ManyToManyField
        return [book.title for book in books]
    except Library.DoesNotExist:
        return f"Library '{library_name}' not found."

# 3. Retrieve the librarian for a library using `filter()`
def get_librarian_for_library(library_name):
    try:
        librarian = Librarian.objects.filter(library__name=library_name).first()  # Using filter() here with OneToOneField
        return librarian.name if librarian else "No librarian found for this library."
    except Librarian.DoesNotExist:
        return f"No librarian found for the library '{library_name}'."

# Testing the queries
if __name__ == "__main__":
    print("Books by Author 'J.K. Rowling':", get_books_by_author("J.K. Rowling"))
    print("Books in Library 'City Library':", get_books_in_library("City Library"))
    print("Librarian for 'City Library':", get_librarian_for_library("City Library"))
