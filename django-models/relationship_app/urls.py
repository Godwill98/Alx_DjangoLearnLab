from django.urls import path
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView,RegisterView
from relationship_app.views import list_books, LibraryDetailView

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful! You are now logged in.')
            return redirect('list_books')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

urlpatterns = [
    # Function-based and class-based views
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication views
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'), 
    path('logout/', UserLogoutView.as_view, template_name='logout'),
    path('register/', views.register, name='register'),  # Add URL for user registration.
    path('register/', views.UserRegisterView.as_view(), template_name='register'),  # Add URL for user registration.
    path('admin_view/', views.admin_view, name='admin_view'),
    path('librarian_view/', views.librarian_view, name='librarian_view'),
    path('member_view/', views.member_view, name='member_view'),  # Add URL for member view.
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),  # Add URL for book deletion.  # Add URL for book deletion.  # Add URL for book deletion.  # Add URL for book deletion.  #
]
]