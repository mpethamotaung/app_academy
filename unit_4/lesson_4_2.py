# Storang and Access: Dictionaries
# A dictionary stores key-value pairs

contact = {
    "name":"Amara", #key = name | value = Amara
    "phone":"071 234 5678"
}

print(contact["name"]) # access values by key
print(contact["phone"])
print("-" * 12)
# Use .get('key'): for safe access
# It returns None instead of crashing if the key doesn't exist
print(contact.get("name"))
# .keys(): returns all available keys
print(contact.keys()) 
# .value(): returns all available values
print(contact.values())
# .items(): returns (key, value) pairs for iteration
print(contact.items())
