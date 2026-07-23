#Logical Operators are used to build complex rules and conditions
price = 25
#The 'and' operator: evaulates to true if both conditions are true
print(price > 10 and price < 30) #If both are true the result will be true

# The 'or' operator: evaluates to true if 1 condition is met
price = 5
print(price > 10 or price <30) #if one is true, the result will be true

#The 'not' operator: inverses any given values
price = 5
print(price > 10) #returns True
print(not price > 10) #returns False