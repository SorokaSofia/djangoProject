from django.test import TestCase, Client
from django.urls import reverse
from .models import Recipe, Category

class RecipeViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name='TestCategory')
        for i in range(20):
            Recipe.objects.create(name=f'Recipe {i}', description='Delicious food', category=self.category)

    def test_main_view(self):
        response = self.client.get(reverse('recipe:main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe/main.html')
        self.assertEqual(len(response.context['recipes']), 20)

    def test_category_detail_view(self):
        response = self.client.get(reverse('recipe:category_detail', args=[self.category.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe/category_detail.html')
        self.assertEqual(len(response.context['recipes']), 20)
        self.assertEqual(response.context['category'], self.category)
