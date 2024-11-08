from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Fetch all book records
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-based view to display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# User Login View (built-in)
class UserLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# User logout View (built-in)
class UserLogoutView(LogoutView):
    template_name = 'relationship_app/login.html'


class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')
