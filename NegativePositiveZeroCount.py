negative_Count = 0
positive_Count = 0
zero_Count = 0
counter = 0

number = int(input('Enter any number or ctrl + z to quit: '))

while number != "ctrl + z":
	if number < -1:
		negative_Count +=1
	if number > 0:
		positive_Count +=1
	if number == 0:
		zero_Count +=1
	counter += 1
	number = int(input('Enter any number or -1 to quit '))

print('The number of positive integers entered are ', positive_Count)
print('The number of negative integers entered are ', negative_Count)
print('The number of zeros entered are ', zero_Count)