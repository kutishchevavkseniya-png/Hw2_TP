from Ingredient import Ingredient
class Recipe:
    def __init__(self, title: str, ingredients=None):
        self.title = title
        self.ingredients = ingredients if ingredients is not None else []
        
    def add_ingredient(self, ingredient: Ingredient):
        for ingr in self.ingredients:
            if ingr == ingredient:
                    ingr.quantity += ingredient.quantity
                    break
            else:
                self.ingredients.append(ingredient)
    @staticmethod
    def is_valid_ratio(ratio):
        try:
            return float(ratio) > 0
        except (TypeError, ValueError):
            return False
    
    def scale(self, ratio: float):
        if not self.is_valid_ratio(ratio):
            raise ValueError("Ошибка: мы не можем умножать на отрицательное число, так ничего не приготовить")
        new_recipe = []
        for i in self.ingredients:
            a = Ingredient(i.name, i.quantity * ratio, i.unit)
            new_recipe.append(a)
        return Recipe(self.title, new_recipe)
    
    def __len__(self):
        return len(self.ingredients)
    
    def __str__(self):
        string = self.title + ":\n"
        for ingr in self.ingredients:
            string = string + str(ingr) + "\n"
        return string