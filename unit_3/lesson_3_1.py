#Calculating the tip

bill = float(input("Enter the total bill: R"))
tip = 0.15 # 15% written in decimal

value_tip = bill * tip # one astericks (*) multiplication, and double astericks (**) to the power of
total_cost = bill + value_tip

print(f"Here is the tip: {value_tip}")
print(f"Here is the tip: {round(value_tip,2)} rounded") 
#round takes in 2 arguments (number, ndigits)
'''
number: The integer or float value to round
ndigits: The number of decimal places to round to
'''

print(f"Here is total cost: {total_cost}")
print(f"Here is total cost: {round(total_cost, 2)} rounded")
