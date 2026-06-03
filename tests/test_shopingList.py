import pytest
from Ingredient import Ingredient
from Recipe import Recipe
from ShoppingList import ShoppingList

def test_add_recipe():
    recipe = Recipe("Салат", [Ingredient("черемша", 67, "г")])
    cart = ShoppingList()
    cart.add_recipe(recipe, 2)
    result = cart.get_list()
    assert len(result) == 1
    assert result[0].quantity == 134

def test_invalid_portions():
    recipe = Recipe("Салат")
    cart = ShoppingList()
    with pytest.raises(ValueError, match="Количество порций должно быть положительным"):
        cart.add_recipe(recipe, 0)

def test_remove_recipe():
    recipe1 = Recipe("Салат", [Ingredient("Черемша", 67, "г")])
    recipe2 = Recipe("Торт", [Ingredient("Сгущенка", 69, "г")])
    cart = ShoppingList()
    cart.add_recipe(recipe1, 1)
    cart.add_recipe(recipe2, 1)
    assert len(cart._list) == 2
    cart.remove_recipe("Салат")
    assert len(cart._list) == 1
    assert cart._list[0][1] == "Торт"

def test_get_sums_ingredients():
    recipe1 = Recipe("Салат", [Ingredient("Черемша", 67, "г")])
    recipe2 = Recipe("Торт", [Ingredient("Сгущенка", 69, "г")])
    cart = ShoppingList()
    cart.add_recipe(recipe1, 1)
    cart.add_recipe(recipe2, 1)
    result = cart.get_list()
    assert len(result) == 1
    assert result[0].quantity == 136

def test_shopping_list_addition():
    cart1 = ShoppingList()
    cart2 = ShoppingList()
    cart1.add_recipe(Recipe("Салат", [Ingredient("Черемша", 67, "г")]), 1)
    cart2.add_recipe(Recipe("Торт", [Ingredient("Сгущенка", 69, "г")]), 1)
    cart3 = cart1 + cart2
    assert len(cart3._list) == 2
    assert len(cart1._list) == 1  
    assert len(cart2._list) == 1 

