weight = float(input())
height = float(input())

BMI = weight / (height * height)

print(weight, 'Please enter weight (Kg)')
print(height, 'Please enter height (m)')

if BMI <= 18.5:
    print('your BMI is: ', BMI)
    print('Result is : Underweight :(')
elif 18.5 < BMI <= 25:
    print('your BMI is: ', BMI)
    print('Result is : Normal :)')
elif 25< BMI < 30:
    print('your BMI is: ', BMI)
    print('Result is : Overweight :(')


