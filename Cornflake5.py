count = 0
total = 0
number = int(input('Enter a number'))
while number != 0:
	number = int(input('Enter a number'))
	total += number
	count += 1
if count != 0:
	average = total / count 
	print('The average is', average)