print("Welcome to Negar's BMI calculator ! :D ")

print('Please enter your weight(Kg):')
weight = float(input())
print('Almost there, now please enter your height(m):')
height = float(input())

BMI = weight / (height * height)


if BMI <= 18.5:
    print('your BMI is: ', BMI)
    print('Result is : Underweight :(')
elif 18.5 < BMI <= 25:
    print('your BMI is: ', BMI)
    print('Result is : Normal :)')
elif 25 < BMI < 30:
    print('your BMI is: ', BMI)
    print('Result is : Overweight :(')
else:
    print('your BMI is: ', BMI)
    print('Result is : Obesity :((')


