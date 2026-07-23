#Example of a formatted table

sample_data = [
    {"Name": "Alice", "Age": 30, "Occupation": "Engineering"},
    {"Name": "Bob", "Age": 24, "Occupation": "Engineering"},
    {"Name": "Charlie", "Age": 29, "Occupation": "Engineering"},
    {"Name": "David", "Age": 35, "Occupation": "Engineering"},
]

print(f"{'Name':<10} {'Age':<5} {'Occupation':<15}")
print("-" * 30)

for person in sample_data:
    print(f"{person['Name']:<10} {person['Age']:<5} {person['Occupation']:<15}")