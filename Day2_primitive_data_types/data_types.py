# Data types

#substring (grep the charecter from a string based on charecters starting from 0)
print("############################################################")
# example
street_name = "Abbey Road"
print("The substring result is : " + street_name[4] + street_name[7])

print("############################################################\n")
# integer
# example
print("Integer")
a = 5
b = 7
print("The data type of a = 5 , b = 7 is :", type(a), type(b))
print("The addition of a + b result is")
print(a + b)

print("############################################################\n")

###############################################################################################

# Program to get two digit values as inputs and add the two digits:

print("Program to get two digit values as inputs and add the two digits:")
two_digit_number = input("Type a two digit number: ")

#Steps:

# Convert input value to string
values = str(two_digit_number)

# create substring variables to get the value of first ans second digit
first_str = values[0]
second_str = values[1]

# convert the substring values to int for addition program
first_int = int(first_str)
second_int = int(second_str)

# perform addition of the result value
result = first_int + second_int

# convert the result int to string in the print
print("The addition of " + first_str + " and " + second_str + " is : " + str(result))
print("############################################################\n")
##########################################################################################

