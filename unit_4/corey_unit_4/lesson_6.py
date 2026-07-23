# Dictionaries (hashmpas/associative arrays) allow us to work key-value pairs
"""
key-value pairs: two linked values where the key is a unique identifier 
where we can find our data and the value is that data. Example in a dictionary
the word to be looked up would be the key and the definition of that word,
would be the value
"""

student = {
    'name': 'Robin',
    'age': 682,
    'courses': ['History', 'Archeology', 'Flowers']
}

print(student) # Prints all values and keys of variable 'student'
print(student['name']) # Access key

"""
.get(): method that is a better way to get values or kesy from dict 
because if key does not exist, will return None
'Not Found': in the get method you parse in the key and a defualt value, returns the value
if no defualt value is parsed, returns None
"""
print(student.get('phone', 'Not found')) 


print(student.keys()) # returns keys of variable student
print(student.values()) # returs values of variable student

#Add key and value/Update value of key
student['phone'] = '0765874265'
print(student)

# .update(): method takes in a dictionary as an argument
student.update({'name': 'Zoro', 'age':42,})
print(student)

# del : keyword for deleting key-value pair
del student['courses']
print(student)

# .pop(): method, will remove and also return the value
popped = student.pop("age")
print(popped)
print(student)

# loop through keys and values in dictionary
student = {
    'name': 'Robin',
    'age': 682,
    'courses': ['History', 'Archeology', 'Flowers']
}

print(len(student)) # Returns number of keys
print(student.items()) #print all items in the dictionary (pairs)

#looping through dictionaries
for key,value in student.items():
    print(key, value)