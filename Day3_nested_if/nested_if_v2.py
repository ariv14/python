# Requirements 2:
# Height to ride roller coaster: 120 cm
# Age and ticker price (Age below 12 $5 | Age between 12 and 18 is $7 | Age above 18  $12 )

print("Welcome to the roller coaster\n")

height = int(input("What is your height:\n"))

if height >= 120:
    print("You are allowed to ride!!")
    age = int(input("What is your age:\n"))
    if age < 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("You have to grow 120 cm to ride")
