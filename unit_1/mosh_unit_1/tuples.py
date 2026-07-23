"""Tuples are kind of like lists, we use them to store a sequence of objects
but tuples are immutable. Meaning that we cannot change them once created

-We use Tuples to prevent accidental modification of a list"""
numbers = (1, 2, 3, 3) #We use round braces for tuples
print(numbers.count(3)) #Returns number of occurances of an element
print(numbers.index(3)) #Returns the index of the first occurance of the given element
