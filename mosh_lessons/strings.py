#Strings

#course is a variable and string is an object
course = 'Python for Beginners'
#print, int and other are general purpose functions
# methods are functions that are object dependent (replace, upper, capitalize, etc.)
#upper(): converts string to upper case,
print(course.upper())
print(course)
#lower(): converts string to lowercase,
print(course.lower())
#find(): checks if string contains character/sequence of characters
print(course.find("h")) #Returns 3 because the first character in a string is zero
#find(): parse a sequence of characters
print(course.find("for"))
#replace(): Replacing a string of something to something else
#Strings are immutable
print(course.replace("for", "4"))
#Special Keyword in Python (in, for, etc.)
print("Python" in course)