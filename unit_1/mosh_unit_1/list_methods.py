#list are objects with methods
numbers = [1, 2, 3, 4, 5]
#append(): Add a number at the end of a list
numbers.append(6) 
print(numbers)

#insert():Add a number anywhere in the list
numbers.insert(0, -1) #Insert expects index number and value
print(numbers)

#remove(): Remove a number from the list
numbers.remove(3)
print(numbers)
#reverse(): inverts the list
numbers.reverse()
print(numbers)

#clear(): Remove all items in a list
numbers.clear()
print(numbers)

#IN operator: if an item exists in a list or not
numbers = [1, 2, 3, 4, 5]
print(1 in numbers) #returns true because 1 is in the list

#len(): Built-in function, return the number of items in the list
print(len(numbers))