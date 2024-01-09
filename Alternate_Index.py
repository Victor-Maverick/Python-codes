array = [1, 2, 3]
my_array = ['a', 'b', 'c']

new_array = my_array 

index=0
count=0
for count in range(len(array) + len(my_array)):
	new_array[count] = my_array[index]
	count+=2
	index+=1

 

print(new_array)