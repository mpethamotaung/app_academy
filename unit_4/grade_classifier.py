# Building a student grade classifier

print("Welcome to the grade classifier")
print("=" * 30)
# 1. Collect learner credentials
first_name = input("Enter your name first name: ")
last_name = input("Enter your last name: ")
full_name = f"{first_name} {last_name}"

# Collect learner marks
math_mark = float(input("Enter your maths marks: "))
phys_mark = float(input("Enter Physics marks: "))
code_mark = float(input("Enter your coding marks: "))

# 2. Calculate the average mark across the three subjects
average_mark = (math_mark + phys_mark + code_mark)//3


# 3. Assign a letter grade
if average_mark >= 80:
    grade = 'A'
elif average_mark >= 70:
    grade = 'B'
elif average_mark >= 60:
    grade = 'C'
elif average_mark >=50:
    grade = 'D'
else: #all conditions are false
    grade = 'F'

# 4. Assign Pass if above 50, else fail
if average_mark > 50:
    status = 'pass'
else:
    status = 'fail'

# 5. flag subject below 40
needs_intervention = (math_mark < 40) or (phys_mark < 40) or (code_mark < 40)




# 6. Display formatted report card
print("=" * 66)
print("=" * 66)
print(f"{'REPORT CARD'} of: {full_name.title()}")
print("-" * 66)
print("Grade Chart: A (80+), B (70-79), C (60-69), D (50-59), F (below 50)")
print("-" * 66)
width = 20
print(f"{'Subject':<{width}}   | {'Mark':<{width}}")
print("-" * 66)
print(f"Mathematics Mark:     | {math_mark}")
print(f"Physics Mark:         | {phys_mark}")
print(f"Coding Mark:          | {code_mark}")
print(f"{'Overall Average:'}      | {average_mark}")
print(f"Grade:                | {grade}")
print(f"Status:               | {status}" )
print("=" * 66)

#needs intervention
if needs_intervention:
    print(f"{'Needs intervention, one or more marks below 40':^66}")
else:
    print(f"{'Good Performance':^66}")

print("-" * 66)

