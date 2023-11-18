password = str(input('Enter your password: '))
stars = len(password)* '*'

print (stars)

age = int(input('Enter your age'))

if age > 18:
	print ('eligible')
if age < 18:
	print('not eligible')

name = input('enter your name: ')
if name:
	print('your name is ', name)