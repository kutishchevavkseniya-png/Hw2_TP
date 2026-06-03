import pytest
from Ingredient import Ingredient
from Recipe import Recipe
from ShoppingList import ShoppingList
from DietaryRecipe import DietaryRecipe

def test_recipe_create():
    ing = Ingredient("Черемша", 67, "г")
    recipe = Recipe("Салат", [ing])
    assert recipe.title == "Салат"
    assert len(recipe) == 1

def test_add_ingredient():
    recipe = Recipe("Салат")
    ing = Ingredient("Черемша", 67, "г")
    recipe.add_ingredient(ing)
    assert len(recipe) == 1
    assert recipe.ingredients[0].quantity == 67

def test_ingredient_merge():
    recipe = Recipe("Салат")
    recipe.add_ingredient(Ingredient("Черемша", 67, "г"))
    recipe.add_ingredient(Ingredient("Газан", 69, "г"))
    assert len(recipe) == 1
    assert recipe.ingredients[0].quantity == 136

def test_scale():
    recipe = Recipe("Салат", [Ingredient("Черемша", 67, "г")])
    scaled = recipe.scale(2)
    assert scaled is not recipe
    assert scaled.ingredients[0].quantity == 134
    assert recipe.ingredients[0].quantity == 67  

def test_scale_invalid_info():
    recipe = Recipe("салат", [Ingredient("черемша", 67, "г")])
    with pytest.raises(ValueError):
        recipe.scale(0)
    with pytest.raises(ValueError):
        recipe.scale(-1)