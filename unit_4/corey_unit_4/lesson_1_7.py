"""Python provides two distinct wasy to sort data:
1. list.sort() method | modify original data
2. sorted() function | create new sorted copy
"""

# Using list.sort() | in place modifcation
numbers = [5, 2, 9, 1]
numbers.sort()
print(numbers)
# Output: [1, 2, 5, 9]

#Using sorted() function | Creates a copy of the sorted
letters = ["c", "a", "b"]
new_letters = sorted(letters)
print(letters) # Output: ["c", "a", "b"] | returns original list
print(new_letters) #Output: ["a", "b", "c"] | returns sorted copy of original list