#Complex types 
#List of numbers, objects, names, etc.
#We use square brackets for lists
names = [ "Luffy", "Zoro", "Jimbe", "Sanji", "Chopper"]
print(names)
#print a specific object in a list
print(names[0]) #prints first element of the list
#List splicing
print(names[2:]) #prints list items from index 2
print(names[-1]) #prints last element of the list
print(names[-2]) #prints 2nd last element of the list
print(names[0:3]) #prints first element until 2nd element (index + 1)

#replacing list elements
names[0] = "Monkey D. Luffy"
print(names)