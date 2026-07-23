# is: checks object identity (keyword to check if values have the same ID/same object in memory)

a = [1, 2, 3]
b = [1, 2, 3]

print(id(a)) #id() check the id of an variable in memory
print(id(b))
print(a is b) # Returns false, because they are different objects in memory

a = [1, 2, 3]
b = a
print(id(a)) #id() check the id of an object in memory
print(id(b))
print(a is b) # Returns true, because they are the same object in memory
print(a == b) # Returns true, because b equals to a
print(id(a) == id(b)) # Returns true, because they are the object in memory
