from book import Book
from recipe import Recipe

book = Book('Mon Livre')
print(book.name)

rec1 = Recipe("crepes", 1, 60, ["farine", "lait", "oeufs"], "les crepes c'est booong", "dessert")
rec2 = Recipe("salade", 2, 10, ["radis", "laitue"], "green green green", "starter")
rec3 = Recipe("crepes2", 1, 60, ["farine", "lait", "oeufs", "fromage"], "les crepes c'est booong aussi en entree", "starter")

book.add_recipe(rec1)
book.add_recipe(rec2)
book.add_recipe(rec3)
book.get_recipe_by_name("crepes")
book.get_recipes_by_types("starter")
book.get_recipes_by_types("lunch")
book.add_recipe(5)
