from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class TimeStampMixin(models.Model):
    """Реализация атрибутов времени создания и обновления записи"""

    created_at = models.DateTimeField("Время создания записи", auto_now_add=True)
    updated_at = models.DateTimeField("Время обновления записи", auto_now=True)

    class Meta:
        abstract = True


class Recipe(TimeStampMixin):
    """Рецепт"""
    recipe_name = models.CharField("Название рецепта", max_length=50, null=False)
    recipe_description = models.CharField("Описание рецепта", max_length=1000, null=False)
    prep_time = models.CharField("Время приготовления", max_length=10, null=False)

    def __str__(self):
        return f'{self.recipe_name}\n{self.recipe_description}\n{self.prep_time}'

    class Meta:
        app_label = "recipes"
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"


class Category(TimeStampMixin):
    """Категория"""
    food_category = models.CharField("Категория", max_length=50, null=False)
    cuisine = models.CharField("Направление кухни", max_length=50, null=False)

    def __str__(self):
        return f'{self.food_category}\n{self.cuisine}'

    class Meta:
        app_label = "recipes"
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Ingredients(TimeStampMixin):
    """Ингредиенты"""

    ingredient_name = models.CharField("Название ингредиента", max_length=50, null=False)

    def __str__(self):
        return self.ingredient_name

    class Meta:
        app_label = "recipes"
        verbose_name = "ингредиент"
        verbose_name_plural = "ингредиенты"


class Quantity(TimeStampMixin):
    """Количество"""

    ingredient_quantity = models.CharField("Количество ингредиентов", max_length=50, null=False)

    def __str__(self):
        return f"{self.ingredient_quantity}"

    class Meta:
        app_label = "recipes"
        verbose_name = "количество"
        verbose_name_plural = "количество"


class Measurements(TimeStampMixin):
    """Единицы измерения"""

    measurement_name = models.CharField("Ед. измерения", max_length=1000, null=False)

    def __str__(self):
        return f"{self.measurement_name}"

    class Meta:
        app_label = "recipes"
        verbose_name = "ед. измерения"
        verbose_name_plural = "ед. измерения"


class RecipeSteps(TimeStampMixin):
    """Этапы"""

    step_description = models.CharField("Описание этапа", max_length=1000, null=False)

    def __str__(self):
        return f"{self.step_description}"

    class Meta:
        app_label = "recipes"
        verbose_name = "этап"
        verbose_name_plural = "этапы"
