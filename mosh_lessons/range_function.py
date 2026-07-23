# Range(): Builtin function in python is used to generate a sequence of numbers

numbers = range(5) #this will return a range object (0 to 5, excluding 5)
print(numbers) #returns 'range(0,5)' default representation of a range object
print("------")

for number in numbers:
    print(number)
print("------")

numbers = range(5, 10) #5 represents starting number and 10 represents the ending number excluding 10
for number in numbers:
    print(number)
print("------")

numbers = range(5, 10, 2) #5 starting, 10 ending, 2 step
for number in numbers:
    print(number)
print("------")

for number in range(5):
    print(number)