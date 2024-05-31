from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from .models import Recipe
import random

def main(request):
    recipes = list(Recipe.objects.all())
    random_recipes = random.sample(recipes, min(len(recipes), 10))
    return render(request, 'recipe/main.html', {'recipes': random_recipes})


def category_detail(request):
    return render(request, 'recipe/category_detail.html')