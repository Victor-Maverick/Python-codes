name = '1234565321'

array = []
array[:] = name



for i in array:
	if array[0] == array[-1] and array[1] == array[-2]:
		print('this is a palindrome')
		break;
	else:
		print('not a palindrome')
		break