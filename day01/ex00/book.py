import datetime
from recipe import Recipe

class Book:
	def __init__(self, name):
		self.name = name
		self.last_update = datetime.datetime.now() 
		self.creation_date = datetime.datetime.now()
		self.recipes_list = {
			"starter" : {},
			"lunch" : {},
			"dessert" : {}
		}

	def get_recipe_by_name(self, name):
		"""Print a recipe with the name `name` and return the instance"""
		for type in self.recipes_list:
			for recipe in self.recipes_list[type]:
				if recipe == name:
					inst = self.recipes_list[type][recipe]
					print(str(inst))
					return inst

	def get_recipes_by_types(self, recipe_type):
		"""Get all recipe names for a given recipe_type """
		s = ', '.join(recipe for recipe in self.recipes_list[recipe_type])
		print(s)

	def add_recipe(self, recipe):
		"""Add a recipe to the book and update last_update"""
		if isinstance(recipe, Recipe):
			self.recipes_list[recipe.recipe_type][recipe.name] = recipe
		else: print("ERROR : not a recipe")
