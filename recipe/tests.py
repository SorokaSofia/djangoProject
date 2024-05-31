from django.test import TestCase
from django.urls import reverse
from .models import Recipe, Category


class MainViewTests(TestCase):

    def setUp(self):
        # Создаем категорию для рецептов
        self.category = Category.objects.create(name='Desserts')

        # Создаем несколько объектов Recipe для тестирования
        for i in range(15):
            Recipe.objects.create(
                title=f'Recipe {i}',
                description='Sample description',
                instructions='Sample instructions',
                ingredients='Sample ingredients',
                category=self.category
            )

    def test_main_view_status_code(self):
        response = self.client.get(reverse('recipe:main'))
        self.assertEqual(response.status_code, 200)

    def test_main_view_template_used(self):
        response = self.client.get(reverse('recipe:main'))
        self.assertTemplateUsed(response, 'recipe/main.html')

    def test_main_view_context(self):
        response = self.client.get(reverse('recipe:main'))
        self.assertTrue('recipes' in response.context)
        self.assertEqual(len(response.context['recipes']), 10)


class CategoryDetailViewTests(TestCase):

    def setUp(self):
        # Создаем категорию и несколько объектов Recipe для тестирования
        self.category = Category.objects.create(name='Desserts')
        for i in range(5):
            Recipe.objects.create(
                title=f'Recipe {i}',
                description='Sample description',
                instructions='Sample instructions',
                ingredients='Sample ingredients',
                category=self.category
            )

    def test_category_detail_view_status_code(self):
        response = self.client.get(reverse('recipe:category_detail', args=[self.category.id]))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_view_template_used(self):
        response = self.client.get(reverse('recipe:category_detail', args=[self.category.id]))
        self.assertTemplateUsed(response, 'recipe/category_detail.html')

    def test_category_detail_view_context(self):
        response = self.client.get(reverse('recipe:category_detail', args=[self.category.id]))
        self.assertTrue('category' in response.context)
        self.assertEqual(len(response.context['category']), 5)
