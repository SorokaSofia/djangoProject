from django.contrib import admin
from .models import Recipe, Category

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category')
    readonly_fields = ('created_at', 'updated_at')  # Припускаючи, що у вас є ці поля

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category)
