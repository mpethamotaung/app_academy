#Loop through values of list

courses = ["History", "Math", "Physics", "CompSci"]

for course in courses:
    print(course) # will loop until all items in the list are printed out

"""enumerate: Access the index and the value
    - Returns 2 values: the index and the value
"""

for index,course in enumerate(courses, start=1): # parse in start argument to start at specific number
    print(index, course) 