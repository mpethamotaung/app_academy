# Collect Data
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
user_bio = input("Tell us about yourself: ").strip()


# Combine first name initial with lastname (e.g. 'tdlamini')
username = f'{first_name[0]}{last_name}'


# Display full name in Title Case using .title() method
full_name = f'{first_name} {last_name}'

# Display all output using f-strings
print(f'\n --- User Information --- ')
print(f"Your user name is: {username.lower()}")
print(f"Your full name is: {full_name.title()}")
print(f"Number of Characters in your bio is: {len(user_bio)}") # count and display number of characters in bio
print(f"Your bio is: {user_bio.replace("I am", "I'm")}") # Replace occurence of 'I am' in the bio with "I'm" using .replace()