# Calculate the circumference of a circle

import math

# Formula: C = 2(pie)r

radius = float(input("Enter the radius of a circle: "))
circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)}cm")