# Creating a professional system email generator

first_name = input("Enter first name: ").strip() #Use strip incase user has blank spaces
last_name = input("Enter last name: ").strip()

username = f"{first_name[0]}.{last_name}" # first index of first name + last name

print(f"Your email is: {username.lower()}@university.co.za")