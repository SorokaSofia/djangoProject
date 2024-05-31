from django.shortcuts import render, get_object_or_404
from .models import Recipe, Category
import random

def main(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe/main.html', {'recipes': recipes})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    recipes = Recipe.objects.filter(category=category)
    return render(request, 'recipe/category_detail.html', {'category': category, 'recipes': recipes})
