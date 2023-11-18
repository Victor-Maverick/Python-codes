numberOne = int(input('Enter the first integer'))
numberTwo = int(input('Enter the second integer'))
numberThree = int(input('Enter the third integer'))

sum = numberOne + numberTwo + numberThree
average = sum / 3
product = numberOne * numberTwo * numberThree
print('The sum of', numberOne, numberTwo, 'and', numberThree, 'is', sum)
print('The average of', numberOne, numberTwo, 'and', numberThree, 'is', average)
print('The product of', numberOne, numberTwo, 'and', numberThree, 'is', product)
max = numberOne
if numberTwo > numberOne:
	max = numberTwo
if numberThree > numberTwo:
	max = numberThree
print(max, 'is the largest number')

min = numberOne
if numberTwo < numberOne:
	min = numberTwo
if numberThree < numberTwo:
	min = numberThree
print(min, 'is the smallest number')