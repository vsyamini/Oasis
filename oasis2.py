weight = float(input('Weight in kilograms:'))
height = float(input('Height in feet:'))
height_m = height * 0.304
print('Your height in meters is:', format(height_m, ".2f"))
BMI = weight / (height_m * height_m)
print('Your BMI is:', format(BMI, ".2f"))
if BMI <= 18.5:
    print('YOU ARE UNDERWEIGHT')
elif 18.5 <= BMI <= 24.9:
    print('YOU ARE NORMAL')
elif 25.0 <= BMI <= 29.9:
    print('YOU ARE OVERWEIGHT')
else:
    print('YOU ARE OBESE')