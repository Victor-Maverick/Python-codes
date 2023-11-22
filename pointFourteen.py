age = int(input('Enter your age in years: '))

heart_Rate = 220 - age

lower_Target_Rate = 50 / 100 * heart_Rate
higher_Target_Rate = 85 / 100 * heart_Rate

print('The maximum heart rate is', heart_Rate)
print('The range of target heart rate is', lower_Target_Rate, '-', higher_Target_Rate)