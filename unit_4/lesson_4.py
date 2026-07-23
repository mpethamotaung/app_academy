# Giving our programs a brain, to learn, adapt
# Security check for entry
# Basic if/else statement script

age = int(input("Enter your age: "))
section_pass = input("Do you have a VIP ticket?: (yes/no) ").lower()

if age >= 18 and section_pass == "yes": #comparison statement | comparison operator >=
    print("Access Granted to the VIP section")
elif age >= 18:
    print("Access granted to General Section")
else: #else: a fall back plan if predecesor fails
    print("Access Denied")