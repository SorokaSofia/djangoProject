from django.test import TestCase
from .models import Category, Recipe

class CategoryModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Desserts")

    def test_category_creation(self):
        self.assertIsInstance(self.category, Category)
        self.assertEqual(self.category.__str__(), self.category.name)

class RecipeModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Desserts")
        self.recipe = Recipe.objects.create(
            name="Chocolate Cake",
            description="Delicious chocolate cake recipe",
            category=self.category
        )

    def test_recipe_creation(self):
        self.assertIsInstance(self.recipe, Recipe)
        self.assertEqual(self.recipe.__str__(), self.recipe.name)
        self.assertEqual(self.recipe.category.name, "Desserts")
