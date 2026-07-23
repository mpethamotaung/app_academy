#Creating basic calculator with arithmetic operations

#Collecting user input
num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))

addition = round(num_1 + num_2, 2)
subtraction = round(num_1 - num_2, 2)
multiplication = round(num_1 * num_2, 2)

if num_2 == 0:
    division = "cannot divide by zero"
    floor_division = "cannot divide by zero"
    modulus = "cannot divide by zero"
else:
    division = (round(num_1 / num_2, 2))
    floor_division = round(num_1 // num_2, 2)
    modulus = round(num_1 % num_2, 2)

# All results in a formatted table using f-string
width = 10

print("-" * 24)
print(f"{'Operation':<{width}} | {'Result':>{width}}")
print("-" * 24)
print(f"{'Addition:':<{width}} | {addition:>{width}}")
print(f"{'Subtract:':<{width}} | {subtraction:>{width}}")
print(f"{'multiply:':<{width}} | {multiplication:>{width}}")
print(f"{'Division:':<{width}} | {division:>{width}}")
print(f"{'FloorDiv:':<{width}} | {floor_division:>{width}}")
print(f"{'Modulus':<{width}} | {modulus:>{width}}")
