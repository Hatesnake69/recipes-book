from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from . import models
# Create your views here.


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
        ingredients_id = int(request.GET.get("ingredient_id"))
    except (ValueError, TypeError):
        ingredients_id = None

    query = Q()
    if recipe_id:
        query.add(
            Q(pk=recipe_id), Q.AND,
        )
    if ingredients_id:
        query.add(
            Q(authors__pk=ingredients_id), Q.AND,
        )

    recipe_objects = Recipe.objects.prefetch_related("authors").filter(query)
    ingredients_lookup = Ingredients.objects.all()
    recipe_lookup = Recipe.objects.all()

    return render(
        request,
        "booklist/books.html",
        {
            "books": recipe_objects,
            "form": {
                "description": "Здесь вы можете ознакомиться с каталогом книг",
                "author": {
                    "title": "Автор",
                    "objects": ingredients_lookup,
                    "selected": ingredients_id,
                },
                "book": {
                    "title": "Наименование",
                    "objects": ingredients_lookup,
                    "selected": recipe_id,
                },
            },
        },
    )