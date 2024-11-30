from django.db import models

# Create your models here.

"""
The Author model represents a writer or creator of books. 
It includes:
- name: A string field to store the author's name.

The Book model represents a written work. It includes:
- title: The title of the book.
- publication_year: The year the book was published.
- author: A ForeignKey field linking to the Author model, establishing a one-to-many relationship.
"""


class Author(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()

    
    def __str__(self):
        return self.title