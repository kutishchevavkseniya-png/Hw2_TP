from Ingredient import Ingredient
from Recipe import Recipe
class ShoppingList:
    def __init__(self):
        self._list = []
    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        right_list = recipe.scale(portions)
        for ingr in right_list.ingredients:
            self._list.append((ingr, recipe.title))
    def remove_recipe(self, title: str):
        new_list= []
        for i in self._list:
            if i[1] != title:
                new_list.append(i)
        self._list = new_list
    def get_list(self):
        to_buy = {}
        for ingredient, recipe_title in self._list:
            key = (ingredient.name, ingredient.unit)
            if key in to_buy:
                to_buy[key] += ingredient.quantity
            else:
                to_buy[key] = ingredient.quantity
        shop_list = []
        for (name, unit), quantity in to_buy.items():
            shop_list.append(Ingredient(name, quantity, unit))
        shop_list.sort(key=lambda x: x.name)
        return shop_list
    def __add__(self, other):
        new_list = ShoppingList()
        new_list._list = self._list.copy() + other._list.copy()
        return new_list