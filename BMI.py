height = float(input("Please enter your height in meters:\n"))
weight = float(input("Please enter your weight in kg:\n"))

bmi = round(weight/height**2)

# print(bmi)

if bmi < 18.5:
    print(f"You have a BMI of {bmi} which means your are underweight.")
elif bmi < 25:
    print(f"You have a BMI of {bmi} which means your have a normal weight.")
elif bmi < 30:
    print(f"You have a BMI of {bmi} which means your are overweight.")
elif bmi < 35:
    print(f"You have a BMI of {bmi} which means your are obese.")
else:
    print(f"You have a BMI of {bmi} which means your are clinically obese.")