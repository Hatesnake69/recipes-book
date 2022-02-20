from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse

from recipes.models import Recipe, Ingredient, Category


def home(request):
    """Главная страница. Редирект на `/books`"""
    response = redirect(reverse("recipes"))
    return response


def recipes(request):
    """Список книг с поиском по названию и автору"""

    try:
        recipe_id = int(request.GET.get("recipe_id"))
    except (ValueError, TypeError):
        recipe_id = None

    try:
        recipe_category_id = int(request.GET.get("ingredient_id"))
    except (ValueError, TypeError):
        recipe_category_id = None

    query = Q()
    if recipe_id:
        query.add(
            Q(pk=recipe_id), Q.AND,
        )
    if recipe_category_id:
        query.add(
            Q(authors__pk=recipe_category_id), Q.AND,
        )

    recipes_objects = Recipe.objects.prefetch_related("category").filter(query)
    category_lookup = Category.objects.all()
    recipes_lookup = Recipe.objects.all()

    return render(
        request,
        "recipes/recipes.html",
        {
            "recipes": recipes_objects,
            "form": {
                "description": "Здесь вы можете ознакомиться с каталогом рецептов",
                "category": {
                    "title": "Категория",
                    "objects": category_lookup,
                    "selected": recipe_category_id,
                },
                "recipe": {
                    "title": "Рецепт",
                    "objects": recipes_lookup,
                    "selected": recipe_id,
                },
            },
        },
    )
