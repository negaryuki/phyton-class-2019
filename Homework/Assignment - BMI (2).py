print("Welcome to Negar's BMI calculator !\n :D ")

print("First, Please tell me, will you use SI units?\n Answer with Yes or No ")

answer = input()

print('Please enter your weight:')
weight = float(input())
print('Almost there, now please enter your height:')
height = float(input())

if answer == 'Yes' or 'yes':
    BMI = weight / (height * height)
    print('and your BMI is: ', BMI)

    if BMI <= 18.5:
        print('Result is : Underweight :(')
    elif 18.5 < BMI <= 25:
        print('Result is : Normal :P Great !')
    elif 25 < BMI < 30:
        print('Result is : Overweight :(')
    else:
        print('Result is : Obesity :,((')

elif answer == 'No'or 'no':
    BMI = weight // (height * height) * 703
    print('and your BMI is: ', BMI)

    if BMI <= 18.5:
        print('Result is : Underweight :(')
    elif 18.5 < BMI <= 25:
        print('Result is : Normal :P Great !')
    elif 25 < BMI < 30:
        print('Result is : Overweight :(')
    else:
        print('Result is : Obesity :,((')
