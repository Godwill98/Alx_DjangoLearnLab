from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import RecipeListCreate, RecipeDetail, RecipeSearch

urlpatterns = [
    path('recipes/', RecipeListCreate.as_view(), name='recipe-list-create'),
    path('recipes/<int:pk>/', RecipeDetail.as_view(), name='recipe-detail'),
    path('recipes/search/', RecipeSearch.as_view(), name='recipe-search'),
    
]   




