number_Of_Years = int(input('enter the number of years'))
amount_Invested = 1000
annual_Rate = 7
annual_Interest= amount_Invested * (1 + annual_Rate)**number_Of_Years

if number_Of_Years == 10:
	print('the money after 10 years will be', annual_Interest)


