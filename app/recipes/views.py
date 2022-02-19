from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from . import models
# Create your views here.


def home(request):
    """Главная страница. Редирект на `/recipes`"""
    return render(request, "recipes/base.html")


def recipes(request):
    """Список книг с поиском по названию и автору"""
    return render(request, "recipes/base.html")
