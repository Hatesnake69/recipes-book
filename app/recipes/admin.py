from django.contrib import admin
from .models import Category, Recipe, Ingredient, Measurement, Quantity



# Register your models here.
admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Measurement)
admin.site.register(Quantity)
