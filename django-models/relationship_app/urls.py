from django.urls import path
from . import views
from .views import list_books,UserLoginView, UserLogoutView



urlpatterns = [
    path('list_books/', views.list_books, name='list_books'),
    path('library_detail/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    #Authentication views
    path('login/', UserLoginView.as_view, template_name='login'),
    path('logout/', UserLogoutView.as_view, template_name='logout'),
]

