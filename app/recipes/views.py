from django.views.generic.list import ListView
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse

from recipes.models import Recipe, Ingredient, Category


def home(request):
    """Главная страница. Редирект на `/recipes`"""
    response = redirect(reverse("recipes:recipes"))
    return response


def categories(request):
    """Список категорий блюд"""
    categories = Category.objects.all()
    context = {'title': 'Категории', 'categories': categories}
    return render(request, 'recipes/categories.html', context)


def category(request, category_id):
    """Категория блюда"""
    category = Category.objects.get(pk=category_id)
    context = {'title': category.food_category, 'category': category}
    return render(request, 'recipes/category.html', context)


def recipe(request, recipe_id):
    """Страница рецепта"""
    recipe = Recipe.objects.get(pk=recipe_id)
    context = {'title': recipe.recipe_name, 'recipe': recipe}
    return render(request, 'recipes/recipe.html', context)


def recipes(request):
    """Список всех рецептов"""
    recipes = Recipe.objects.all()
    context = {'title': 'Рецепты', 'recipes': recipes}
    return render(request, 'recipes/recipes.html', context)


def ingredients(request):
    """Список всех ингредиентов"""
    ingredients = Ingredient.objects.all()
    context = {'title': 'Ингридиенты', 'ingredients': ingredients}
    return render(request, 'recipes/ingredients.html', context)


def ingredient(request, ingredient_id):
    """Список рецептов с участием ингредиента"""
    ingredient = Ingredient.objects.get(pk=ingredient_id)
    context = {'title': ingredient.ingredient_name, 'ingredient': ingredient}
    return render(request, 'recipes/ingredient.html', context)


class SearchView(ListView):
    """Страница с результатами запроса в поисковой строке"""
    model = Recipe
    template_name = 'recipes/search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = Recipe.objects.filter(recipe_name__contains=query)
            result = postresult
        else:
            result = None
        return result
