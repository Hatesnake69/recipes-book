from django.urls import path

from . import views

app_name = 'recipes'
urlpatterns = [
    path("", views.home, name="home"),
    path("categories/", views.categories, name="categories"),
    path('categories/<int:category_id>', views.category, name="category"),
    path("recipes", views.recipes, name="recipes"),
    path('recipes/<int:recipe_id>', views.recipe, name="recipe"),
    path('ingredients', views.ingredients, name="ingredients"),
    path('ingredients/<int:ingredient_id>', views.ingredient, name="ingredient"),
    path('search/', views.SearchView.as_view(), name="search")
]
