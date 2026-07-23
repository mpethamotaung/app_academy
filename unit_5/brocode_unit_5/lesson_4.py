# Calculate the area of the circle

import math

radius = float(input("Enter the radius of a circle: "))

# Formula A = (pie)r**2

area = math.pi * pow(radius, 2)

print(f"The area of the circle is: {round(area, 2)}cm^2")