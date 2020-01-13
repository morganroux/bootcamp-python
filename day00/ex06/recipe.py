
cookbook =	{	
	'sandwich' : {
		'ingredients' : ['ham', 'bread', 'cheese', 'tomato'],
		'meal' : 'lunch',
		'prep_time' : 10 
	},
	'cake' : {
		'ingredients' : ['floor', 'sugar', 'eggs'],
		'meal' : 'dessert',
		'prep_time' : 60
	},
	'salad' : {
		'ingredients' : ['avocado', 'arugula', 'tomatoes', 'spinach'],
		'meal' : 'lunch',
		'prep_time' : 15 
	}
}

def print_recipie(recipie=''):
	global cookbook
	print("---")
	print("Recipie for {0}\nIngredient list : {1[ingredients]}\nTo be eaten for {1[meal]}\nTakes {1[prep_time]} minutes to cook".format(recipie, cookbook[recipie]))
	print("---")

def add_recipie(recipie='', ingredients='', meal='', prep_time=''):
	global cookbook
	cookbook[recipie] = {
		'ingredients' : ingredients,
		'meal' : meal,
		'prep_time' : prep_time
	}

def del_recipie(recipie=''):
	global cookbook
	del cookbook[recipie]

def print_cookbook():
	global cookbook
	print("===========")
	print("MY COOKBOOK")
	for recipie in cookbook:
		print_recipie(recipie)
	print("===========")

def	prompt_add():
	lst = []
	rec = input("Name of the recipie : ")
	ing = input("List of the ingredients (blank to skip) : ")
	while ing != '':
		lst.append(ing)
		ing = input('> ')
	meal = input("Meal : ")
	time = input("Prep time : ")
	add_recipie(rec, lst, meal, time)
	pass

def prompt_del():
	rec = input("Recipie to del : ")
	del_recipie(rec)

def prompt_print():
	rec = input("Recipie to print : ")
	print_recipie(rec)

def prompt_exit():
	print("Cookbook closed")
	exit()

def print_error():
	print("""
This option does not exist, please type the corresponding number.
To exit, enter 5.""")

def prompt():
	s = input("""
Please select an option by typing the corresponding number:
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit\n>> """)

	if s == '1': prompt_add()
	elif s == '2': prompt_del()
	elif s == '3': prompt_print()
	elif s == '4': print_cookbook()
	elif s == '5': prompt_exit()
	else: return 0
	return 1

while True:
	if prompt() == 0:
		print_error()
		
