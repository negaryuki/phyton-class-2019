print("Welcome to Negar's BMI calculator !\n (^o^)/")

print('Please enter your weight(Kg):')
weight = float(input())
print('Almost there, now please enter your height(m):')
height = float(input())

BMI = weight / (height * height)
print('and your BMI is: ', BMI)

if BMI <= 18.5:
    print('Result is : Underweight :(')
elif 18.5 < BMI <= 25:

    print('Result is : Normal :) Great !')
elif 25 < BMI < 30:

    print('Result is : Overweight :(')
else:

    print('Result is : Obesity :,((و')


