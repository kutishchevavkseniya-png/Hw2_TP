import pytest
from Ingredient import Ingredient

def test_ingredient_create():
    ing = Ingredient("Соль", 67, "г")
    assert ing.name == "Соль"
    assert ing.quantity == 67
    assert ing.unit == "г"

def test_ingredient_look():
    ing = Ingredient("Квашонка", 3, "л")
    assert str(ing) == "Квашонка: 3.0 л"

def test_ingredient_same():
    ing1 = Ingredient("соль", 67, "г")
    ing2 = Ingredient("соль", 67, "г")
    ing3 = Ingredient("Хлеб", 1984, "г")
    assert ing1 == ing2 
    assert ing1 != ing3  

def test_ingredient_quantity():
    ing = Ingredient("хлеб", 1984, "г")
    with pytest.raises(ValueError, match="Количество должно быть положительным"):
        ing.quantity = -10
