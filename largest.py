number1 = int(input('Enter the first integer: '))
number2 = int(input('Enter the second integer: '))
number3 = int(input('Enter the third integer: '))

if number1 > number2 and number1 > number3:
	print(number1, 'is the largest')
if number1 < number2 and number2 > number3:
	print(number2, 'is the largest')
if number3 > number2 and number3 > number1:
	print(number3, 'is the largest')