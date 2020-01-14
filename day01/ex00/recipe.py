class Recipe:
	def check_inputs(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
		return 1

	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
		if self.check_inputs(name, cooking_lvl, cooking_time, ingredients, description, recipe_type) == 0: exit()
		self.name = name
		self.cooking_lvl = cooking_lvl
		self.cooking_time = cooking_time
		self.ingredients = ingredients
		self.description = description
		self.recipe_type = recipe_type

	def __str__(self):
		txt =	f"---\n\
Recipie for {self.name}\n\
Ingredient list : {self.ingredients}\n\
To be eaten for {self.recipe_type}\n\
Takes {self.cooking_time} minutes to cook\n\
Level : {self.cooking_lvl}\n\
Description : {self.description}\n\
---"
		return txt
