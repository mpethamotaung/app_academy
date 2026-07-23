# 1. Collect
first_name = input("What is your first name?: ")
surname = input("What is your surname?: ")
age = int(input("What is your age?: "))
favourite_number = float(input("What is your favourite number?: "))

# 2. Full name  and Greeting
full_name = first_name + " " + surname
print(f"Welcome, {full_name}!")

# 3. Display name in uppercase and title case
print(f"full name in UPPERCASE: {full_name.upper()}")
print(f"full name in TITLE CASE: {full_name.title()}")

#4. Calculate age in months
age_in_months = age * 12
print(f"Age in Months: {age_in_months}")

# 5. Round the favourite number to 2 decimal places
rounded_number = round(favourite_number, 2)
print(f"Favourite number rounded of to 2 decimals: {rounded_number}")

# Print data types of each collected value using type() 
print(f"Type of first_name: {type(first_name)}")
print(f"Type of surname: {type(surname)}")
print(f"Type of age: {type(age)}")
print(f"Type of favourite number: {type(favourite_number)}")