number = 0
square = 0
cube = 0
print('number\tsquare\tcube')
for number in range(0, 6):
	square = number** 2
	cube = number ** 3
	print('{0:6d}\t{1:6d}\t{2:4d}'.format(number, square, cube))
	