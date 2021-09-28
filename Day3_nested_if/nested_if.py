# Roller coaster company project

# Requirements 1:
# Height to ride roller coaster: 120 cm
# Age and ticker price (Age above 18  $12 | Age below 18 $7)

print("Welcome to the roller coaster\n")

height = int(input("What is your height:\n"))

if height >= 120:
    print("You are allowed to ride!!")
    age = int(input("What is your age:\n"))
    if age >= 18:
        print("Please pay $12")
    else:
        print("Please pay $7")
else:
    print("You have to grow 120 cm to ride")


