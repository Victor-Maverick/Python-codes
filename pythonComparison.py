number1=int(input('Enter first integer'))
number2=int(input('Enter second integer'))
number3=int(input('Enter third integer'))

minimum=number1
if number2<number1:
	minimum=number2

if number3<number2:
	maximum=number3

maximum=number1
if number2>number1:
	maximum=number2

if number3>number2:
	maximum=number3

print('The minimum number is', minimum)
print('The maximum number is', maximum)