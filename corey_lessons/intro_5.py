# LIST SLICING
# access a range of characters | [0:9] including first, excluding last
message = "Hello World"
print(message[0:]) 
print(message[:11]) #same as above, assumes starting index as 0

print(message[6:11]) #prints only the last part of the string
print(message[6:]) #same as above, assumes ending index is end of string