# Body mass index project 2.0
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

# It should tell them the interpretation of their BMI based on the BMI value.

# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

print("Welcome to BMI calculator 2.0\n")

height = input("Enter your height in centimeters : ")
weight = input("Enter your weight in kilograms : ")

bmi = (int(weight) / int(height) / int(height) * 10000)
bmi_as_int = float(bmi)

if bmi_as_int <= 16:
    print(f"Your BMI is {bmi_as_int} , you are severe underweight.")
elif bmi_as_int <= 16.9:
    print(f"Your BMI is {bmi_as_int} , you are moderate underweight.")
elif bmi_as_int <= 18.4:
    print(f"Your BMI is {bmi_as_int} , you are mild underweight.")
elif bmi_as_int <= 24.9:
    print(f"Your BMI is {bmi_as_int} , you are normal.")
elif bmi_as_int <= 29.9:
    print(f"Your BMI is {bmi_as_int} , you are Overweight (Pre-obese).")
elif bmi_as_int <= 34.9:
    print(f"Your BMI is {bmi_as_int} , you are Obese (Class I).")
elif bmi_as_int <= 39.9:
    print(f"Your BMI is {bmi_as_int} , you are Obese (Class II).")
else:
    print(f"Your BMI is {bmi_as_int} , you are Obese (Class III) & above.")