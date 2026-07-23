#Sets are unordered collection of values with no duplicates

courses = {'History', 'Math', 'Physics', 'CompSci'} #Curly braces

print(courses)
#Output: can be unordered, mixed with each iteration and removes duplicates in the set

print('Math' in courses) #Membership test (*optimized*more efficient than list and tuples) | True or False

#Sets can check which values they share with other sets
art_courses = {'History', 'Math', 'Art', 'Design'}

# intersection(): method, checks similarity between sets
print(courses.intersection(art_courses)) # Output: {'History', 'Math'} because both exists in each set

# difference(): method, checks differences between sets
print(courses.difference(art_courses)) #Output: {'Physics', 'CompSci'} 

# union(): method combines sets
print(courses.union(art_courses))

