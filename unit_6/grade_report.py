# Full class grade report generator

students = [
    {'name': 'Mary Anderson', 'maths':85, 'science':78, 'coding':99},
    {'name': 'Bryan Foster', 'maths':99, 'science':78, 'coding':75},
    {'name': 'John Witticker', 'maths':74, 'science':88, 'coding':95},
    {'name': 'Keanu Reeves', 'maths':89, 'science':89, 'coding':100},
    {'name': 'Monkey D. Luffy', 'maths':89, 'science':89, 'coding':100}
]

results = [] # result will store dictionaries output

for student in students:
    name = student['name']
    maths = student['maths']
    science = student['science']
    coding = student['coding']

    average = (maths + science + coding)

    # assign grade according to grade chart (unit 5)
    if average >= 80:
        grade = 'A'
    elif average >=70:
        grade = 'B'
    elif average >= 60:
        grade = 'C'
    elif average >= 50:
        grade = 'D'
    else:
        grade = 'F'

    # assign pass if above 50, else fail
    if average >= 50:
        status = 'pass'
    else:
        status = 'fail'

    # Store result
    results.append({
        'name': name,
        'average': round(average, 2),
        'grade': grade,
        'status': status
    })

# Class statistics
total_average = 0
highest_mark = float('-inf')
lowest_mark = float('inf')

for res in results:

    total_average += res['average']
    if res['average'] > highest_mark:
        highest_mark = res['average']
    if res['average'] < lowest_mark:
        lowest_mark = res['average']

class_average = total_average/len(results)
if results else 0

# Class report
print("=" * 60)
print("CLASS GRADE REPORT")
print("=" * 60)
print(f"{'Name':<20} | {'Average':<10} | {'Grade':<8} | {'Status':<8}")
print("-" * 60)

for res in results:
    print(f"{res['name']:<20} | {res['average']} | {res['grade']:<8} | {res['status']:<8}")

print("-" * 60)
print(f"Class Average: {class_average:.2f}")
print(f"Highest Average: {highest_mark:.2f}")
print(f"Lowest Average: {lowest_mark:.2f}")
print("=" * 60)


# Use while loop for student search
while True:
    print(" --- Student Search --- ")
    search_name = input("Enter student name or 'quit' to exit: ").strip()
    if search_name.lower() == 'quit':
        print("Goodbye!")
        break
    found = False
    for res in results:
        if search_name.lower() in res['name'].lower():
            print(f"Found: {res['name']}")
            print(f" Average: {res['average']}")
            print(f"Grade: {res['grade']}")
            print(f"Status: {res['status']}")
            found = True
            break
    if not found:
        print("No student found with that name. ")

