# Add multiple strins and concatenate them together
greeting = "Hello"
name = "Michael"

#message = f"{greeting}, {name}"
message = greeting + ', ' + name + '. Welcome!' # ', ' string literal
print(message)

'''Formatted string, allows to write the sentence as 
it will appear and put placeholders in place of variables'''
message = f'{greeting}, {name.upper()}. Welcome!'
print(message)