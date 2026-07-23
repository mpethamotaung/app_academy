"""
Title: The Challege, The Phone Directory Search
Description: Create a mini data directory using a list and a dictionary combined
"""

# Create a dictionary called contacts with friend names and phone numbers
contacts = {
    'Sarah':'084 847 3556',
    'Cobey':'068 781 4835',
    'Garp':'065 874 1886'
}

search_name = input("Enter the name of the friend: ").strip().title()

if search_name in contacts:
    print(f"Found! {search_name}'s number is: {contacts[search_name]}")
else:
    print("Contact not found.")