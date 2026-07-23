# Find the hypotenuse of a right angled triangle
# Formula: C = sqrt(a**2 + b**2)

import math

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C is: {c}cm")

