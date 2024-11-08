from django.urls import path
from . import views
from .views import list_books, LibraryDetailView 
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('list_books/', views.list_books, name='list_books'),
    path('library_detail/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    #Authentication views
    path('login/', LoginView.as_view, template_name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]

