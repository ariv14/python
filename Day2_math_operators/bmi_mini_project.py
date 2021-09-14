# Body mass index project

height = input("Enter your height in meters : ")
weight = input("Enter your weight in kilograms : ")

bmi = (weight / height ** 2)
bmi_as_int = int(bmi)
print(bmi_as_int)