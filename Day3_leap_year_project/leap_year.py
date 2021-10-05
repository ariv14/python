# Leap year calculator

print("Leap Year Calculator\n")
year = int(input("Enter the year:\n"))

if (year % 4) == 0:
    if (year % 100) == 0:
        if(year % 400) == 0:
            print("This is leap year")
        else:
            print("This is not a leap year")
    else:
        print("This is leap year")
else:
    print("This is not a leap year")
