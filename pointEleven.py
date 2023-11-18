number = int(input('Enter a five-digit number'))

first_Digit = number % 10
first_Number = number // 10
second_Digit = first_Number % 10
second_Number = first_Number// 10
third_Digit = second_Number % 10
third_Number = second_Number // 10
fourth_Digit = third_Number % 10
fourth_Number = third_Number // 10
fifth_Digit = fourth_Number % 1
fifth_Number = number / 1

print(fourth_Number,  fourth_Digit, third_Digit, second_Digit, first_Digit)
