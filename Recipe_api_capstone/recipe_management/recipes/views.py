from django.shortcuts import render
from rest_framework_simplejwt import views as jwt_views


# Create your views here.
from rest_framework import generics
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

# List and Create Recipes (authenticated users only)
class RecipeListCreate(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically set the user as the creator of the recipe
        serializer.save(user=self.request.user)

# Retrieve, Update, and Delete Recipe (only creator can modify)
class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        # Check if the user is the creator of the recipe
        if serializer.instance.user != self.request.user:
            raise PermissionDenied("You do not have permission to modify this recipe.")
        serializer.save()

    def perform_destroy(self, instance):
        # Check if the user is the creator of the recipe
        if instance.user != self.request.user:
            raise PermissionDenied("You do not have permission to delete this recipe.")
        instance.delete()


from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.permissions import AllowAny

class RecipeSearch(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        query = request.GET.get('query', None)
        recipes = Recipe.objects.all()
        if query:
            recipes = recipes.filter(
                Q(title__icontains=query) | 
                Q(description__icontains=query) | 
                Q(ingredients__icontains=query) |
                Q(category__icontains=query)
            )
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

