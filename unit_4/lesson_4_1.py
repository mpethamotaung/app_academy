#Storang and Access: Lists
# A list is an ordered, mutable collection of value stored in a single variable

students = ['Amara', 'Sipho', 'Lerato']

for student in students:
    print(student)

print("=" * 6)
print(f"Last student: {students[-1]}")

# .append("value"): adds item in list
students.append("Bongani")
print(students)

# Inserting list item .insert(index, item)
students[0] = "Junior"
print(students)

# .remove(item): removes by value
students.remove("Bongani")
print(students)

# .pop(index): removes by index and returns the item
students.pop(2)
print(students)

# len(list): returns the count
print(len(students))