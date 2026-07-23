#Title: The South African Fuel Cost Calculator
print("=" * 45)
print("Let's Calculate your travel cost")
print("=" * 45)

# 1. Ask user how many kilometers they want to drive
kilometers = float(input("How many kilometers do you want to drive? "))
clean_kilometers = round(kilometers, 2)

# 2. Ask user for current petrol price
price_per_liter = float(input("What is the current petrol price: R"))
clean_price = round(price_per_liter, 2)

# 3. Assume car uses 1 liter of fuel for every 10 kilometers driven
liters_needed = clean_kilometers / 10
clean_liters = round(liters_needed, 2)

# 4. Calculate the cost to travel
total_cost = (liters_needed * clean_price)
clean_total_cost = round(total_cost)

# 5. Use type casting to ensure numbers work, and use round() to format the final cost to 2 decimals
print("-" * 45)
print(f"You want to travel a distance of(km): {clean_kilometers} km")
print(f"Current petrol price is: R{clean_price}")
print(f"You need {liters_needed}L of petrol to travel a distance of {clean_kilometers} km.")
print(f"The total cost of your trip is: R{total_cost}")