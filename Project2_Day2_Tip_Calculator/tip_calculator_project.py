# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
print("Welcome to tip calculator !")
bill = float(input("What was the bill amount : "))
persons = int(input("What is the number of persons : "))
tip_percent = int(input("What is the tip percentage you would like to offer (10%, 12% or 15%) : "))
tip_percent_float = tip_percent / 100
bill_with_tip = bill * tip_percent_float + bill
bill_total_each_person = bill_with_tip / persons
# pay_round = round(bill_total_each_person, 2)
# to have two decimal points in result
pay_round = "{:.2f}".format(bill_total_each_person)
print(f"Each person should pay (Bill + tip): {pay_round} ")
