# Body mass index project

height = input("Enter your height in meters : ")
weight = input("Enter your weight in kilograms : ")

bmi = (weight / height ** 2)
bmi_as_int = int(bmi)
print("Your Body Mass Index is : ")
print(bmi_as_int)
print("\n")
print("BMI Categories")
print("Underweight (Severe thinness): < 16.0")
print("Underweight (Moderate thinness): 16.0 - 16.9")
print("Underweight (Mild thinness): 17.0 - 18.4")
print("Normal range: 18.5 - 24.9")
print("Overweight (Pre-obese): 25.0 - 29.9")
print("Obese (Class I): 30.0 - 34.9")
print("Obese (Class II): 35.0 - 39.9")
print("Obese (Class III): 40.0 & above")