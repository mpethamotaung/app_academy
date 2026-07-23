"""
def() function: A built-in keyword used to define a user defined function
function: A block of reusable code place () after the function to invoke it/call it

def fucntion_name(parameters)
    # The code block inside be indeted
    # Perofrm tasks here
    return result

"""

# Defining a function
def happy_birthday(name, age): #the order does matter for arg to be parsed
    print(f"Happy Birthday to {name}")
    print(f"Your age {age} years old!")
    print("Happy birthday to you!")

# Invoking a function
happy_birthday("Thato", 20)
happy_birthday("Hlompho", 24)
happy_birthday("Khwezi", 32)
