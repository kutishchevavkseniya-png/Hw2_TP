from Recipe import Recipe
from Ingredient import Ingredient

class DietaryRecipe(Recipe):
    def __init__(self, title: str, diet_type: str, ingredients=None):
        super().__init__(title, ingredients)
        self.diet_type = diet_type
    
    def scale(self, ratio: float):
        scaled_recipe = super().scale(ratio)
        return DietaryRecipe(scaled_recipe.title, self.diet_type, scaled_recipe.ingredients)
    
    def __str__(self):
        string = f"[{self.diet_type}] {self.title}:\n"
        for ingr in self.ingredients:
            string = string + str(ingr) + "\n"
        return string
