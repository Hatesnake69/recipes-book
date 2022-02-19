from django.db import models


class Category(models.Model):
    """Категория"""
    food_category = models.CharField("Категория", max_length=50, null=False)

    def __str__(self):
        return self.food_category

    class Meta:
        app_label = "recipes"
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Recipe(models.Model):
    """Рецепт"""
    recipe_name = models.CharField(
        "Название рецепта",
        max_length=50,
        null=False
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name="Категория",
        null=False,
        blank=False,
    )
    recipe_description = models.TextField(
        "Описание рецепта",
        max_length=1000,
        null=False
    )
    prep_time = models.CharField("Время приготовления", max_length=50, null=False)

    def __str__(self):
        return self.recipe_name

    class Meta:
        app_label = "recipes"
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"


class Ingredients(models.Model):
    """Ингредиенты"""

    ingredient_name = models.CharField("Название ингредиента", max_length=50, null=False)
    recipe = models.ManyToManyField(
        Recipe, verbose_name="Рецепты",
    )

    def __str__(self):
        return self.ingredient_name

    class Meta:
        app_label = "recipes"
        verbose_name = "ингредиент"
        verbose_name_plural = "ингредиенты"


class Measurement(models.Model):
    """Единицы измерения"""

    name = models.CharField("ед. измерения", max_length=1000, null=False)

    def __str__(self):
        return self.name

    class Meta:
        app_label = "recipes"
        verbose_name = "ед. измерения"
        verbose_name_plural = "ед. измерения"


class Quantity(models.Model):
    """Количество"""
    measurement = models.ForeignKey(
        Measurement,
        on_delete=models.PROTECT,
        verbose_name="ед. измерения",
        null=False,
        blank=False,
    )
    ingredient_quantity = models.IntegerField("Количество ингредиентов",)

    def __str__(self):
        return self.ingredient_quantity

    class Meta:
        app_label = "recipes"
        verbose_name = "количество"
        verbose_name_plural = "количество"





