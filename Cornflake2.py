evenNumbers = 0;
oddNumbers = 0;
for numbers in range(1,100):
	if numbers % 2 == 0:
		evenNumbers += 1
	if numbers % 2 != 0:
		oddNumbers += 1
print('Number of even numbers:', evenNumbers)
print('Number of odd numbers:', oddNumbers)