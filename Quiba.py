number1=int(input('Enter an Integer'))
if number1%5==0 and number1%6==0:
	print ('is', number1, 'divisible by 5 and 6? true')
	print ('is', number1, 'divisible by 5 or 6? true')
	print ('is', number1, 'divisible by 5 or 6? but not both false')
	
elif  number1%5!=0 and number1%6==0:
	print ('is', number1, 'divisible by 5 and 6? false')
	print ('is', number1, 'divisible by 5 or 6? true')
	print ('is', number1, 'divisible by 5 or 6? but not both true')

elif number1%5==0 and number1%6!=0:
	print ('is', number1, 'divisible by 5 and 6? false')
	print ('is', number1, 'divisible by 5 or 6? true')
	print ('is', number1, 'divisible by 5 or 6? but not both true')


elif number1%5!=0 and number1%6!=0:
	print ('is', number1, 'divisible by 5 and 6? true')
	print ('is', number1, 'divisible by 5 or 6? true')
	print ('is', number1, 'divisible by 5 or 6? but not both true')
