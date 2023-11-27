
for numbers in range(1,101,2):
	if numbers > 1:
		if numbers % 3 != 0 and numbers % numbers **0.5 != 0 and numbers % 5 != 0:
			print(numbers, end=" ")