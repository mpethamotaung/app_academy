#The Secure Password Hint Tool

#User to input secret password 
password = input("Enter your password: ")

# Use strip to clean up accidental spaces
clean_password = password.strip()

#print hint using an f-string that forces letters into uppercase so they stand out
password_first_char = clean_password[0].upper()
password_last_char = clean_password[-1].upper()
print(f"Your password hint: It starts with {password_first_char} and ends with {password_last_char}")

