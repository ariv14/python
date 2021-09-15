# Lifetime calculator

print("Lifetime calculator\nEnter your age and maximum expected age\n")
age = input("Enter your age : ")
max_age = input("Enter your maximum lifetime age :")
print("\n")
age_in_months = int(age) * 12
age_in_days = int(age) * 365
age_in_weeks = int(age) * 52
max_age_years = int(max_age)
max_age_months = int(max_age) * 12
max_age_days = int(max_age) * 365
max_age_weeks = int(max_age) * 52
years_left = max_age_years - int(age)
month_left = max_age_months - int(age_in_months)
days_left = max_age_days - int(age_in_days)
weeks_left = max_age_weeks - int(age_in_weeks)
print(f"You have {days_left} days, {weeks_left} weeks and {month_left} months left.")