from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView,RegisterView
from .views import list_books, LibraryDetailView

urlpatterns = [
    # Function-based and class-based views
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication views
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', RegisterView.as_view(template_name = 'relationship_app/register.html'), name='register'),
]
