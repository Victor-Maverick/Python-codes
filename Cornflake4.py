dog_age = int(input("Enter the dog's age in human age: "))

if dog_age == 1 and dog_age == 2:
	dog_age_in_dog_years = dog_age * 10.5
if dog_age > 2:
	dog_age_in_dog_years = (dog_age -2) * 4 + 21
print('The dog\'s age in dog\'s years is', dog_age_in_dog_years)