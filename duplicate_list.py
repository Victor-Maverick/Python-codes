def check_duplicate(my_array):
	new_array = []
	duplicate = []
	for item in range(len(my_array)):
		if my_array[item].count > 1:
			return my_array[item]
		else:
			return print('no duplicates')
	
	#new_array = {x for x in my_array if my_array.count(x)>1}
	#return new_array