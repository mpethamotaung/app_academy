# Range(): function that generates a sequence of numbers
# Takes in start, end(exclusive), and step (skip)

for i in range(5):
    print(i)

# Range with step
for i in range(0, 20, 2): 
    print(i)
# Output: 0, 2, 3, 4 ..., 18

# Range count down
for i in range(10, 0):
    print(i)
# Output: 10, 9, 8 ..., 1

"""
range() function is memory-efficient:
It does not store all numbers in memory, it generates them on demand
"""