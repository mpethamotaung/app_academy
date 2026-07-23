# List Methods (modify)

courses = ["History", "Math", "Physics", "CompSci"] # has length of 4, index 0 to 3 (length of list - 1)
courses_2 = ["Communication", "Windows Programming"] #add these values to courses list

# .insert(): adds list item to specific index/location
courses.insert(0, "Coding") # inserts value into index
print(courses)
courses.insert(0, str(courses_2)) #inserts list in list
print(courses)