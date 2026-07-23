courses = ["History", "Math", "Physics", "CompSci"] # has length of 4, index 0 to 3 (length of list - 1)

# .remove() items from list
del courses[0] #removes the first index in the list
print(courses)

#Useful for stack or queue
courses.pop(1) #removes index 1 | if no index, it removes the last item on list
popped = courses.pop(1)
print(popped) # returns item popped
print(courses)

courses.remove("Math") # removes parsed value
print(courses)