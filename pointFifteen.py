number_One = float(input('Enter a floating-point number'))
number_Two = float(input('Enter a second floating-point number'))
number_Three = float(input('Enter another floating-point number'))

if number_One > number_Two and number_Two > number_Three:
	print(number_Three, number_Two, number_One)

if number_One > number_Three and number_Three > number_Two:
	print(number_Two, number_Three, number_One)

if number_Two > number_One and number_One > number_Three:
	print(number_Three, number_One, number_Two)

if number_Two > number_Three and number_Three > number_One:
	print(number_One, number_Three, number_Two)

if number_Three > number_Two and number_Two > number_One:
	print(number_One, number_Two, number_Three)

if number_Three > number_One and number_One > number_Two:
	print(number_Two, number_One, number_Three)