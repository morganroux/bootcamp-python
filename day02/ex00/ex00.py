def ft_map(f, *args):
	lst = [ f(*[args[j][i] for j in range(len(args))]) for i in range(len(args[0]))]
	return lst
def ft_filter(function_to_apply, list_of_inputs):
    pass
def ft_reduce(function_to_apply, list_of_inputs):
    pass

def f(a, b, c):
	return a + b + c

print(ft_map(f,[1,2],[3,4],[5,6]))

print(list(map(f,[1,2],[3,4],[5,6])))
