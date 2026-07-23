""" Boolean operations (and, or not)
- and: executes if both conditions are true
- or: executes if on condition is true
- not: inverts False to True and True to False
"""

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print("Welcome to the Admin Page")
elif user == "Admin" and not logged_in:
    print("Please loggin to access dashboard")
else:
    print("You do not have access to this page")