#Turn list into strings, separated by a certain value

courses = ["History", "Math", "Physics", "CompSci"]

#.join(): string method parse list as argument
course_str = ", ".join(courses) # Output: History, Math, Physics, CompSci
print(course_str) 

#.split(): converts a string into a list or array of smaller substrings
new_list = course_str.split(", ")
print(new_list)