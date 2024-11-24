from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path,include
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Create a router and register the BookViewSet with it
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),
    
    # Route for BookViewSet for all routes registered with router
    path('', include(router.urls)),
]
