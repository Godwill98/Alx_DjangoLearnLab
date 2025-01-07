from django.contrib import admin

# Register your models here.

from .models import Recipe

# Register Recipe model to appear in the admin interface
admin.site.register(Recipe)
