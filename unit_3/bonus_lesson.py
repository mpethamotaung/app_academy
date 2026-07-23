#Example of a formatted table

name = "Alice"
name_2 = "Bob"

width = 10

#You can add another variable within another set of curly braces
print(f"{name:<{width}}") #Left-aligned within 10 characters
print(f"{name_2:<{width}}")
print("-----------")

print(f"{name:>{width}}") #Right-aligned within 10 characters
print(f"{name_2:>{width}}")
print("-----------")

print(f"{name:^{width}}") # Center-aligned within 10 characters
print(f"{name_2:^{width}}")