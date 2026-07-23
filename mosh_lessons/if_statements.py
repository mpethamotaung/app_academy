#conditions are unlimited, you can have as many as you like
#We use if statements to make decisions in our programs
temperature = 25

if temperature > 30:
    print("It's a hot day")
    print("Drink plenty water")

elif temperature > 20: #temperature is greater than 30 and less than/equal to 30 : (20:30]
    print("It's a nice day")

elif temperature > 10: #temperature is greater than 10 or less than/equal to 20 : (10:20]
    print("It's a bit cold")

else: #executed if none of the above conditions are true
    print("It's a cold day")
print("Done")

#Python uses indentation to represent a block of code, not curly braces {}


