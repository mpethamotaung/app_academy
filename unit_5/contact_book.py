"""
Title: Command-line contact book
description: stores contacts as a list of dictionaries
allows the user to add, search, view, and delete contacts.
This is a foundational data structure pattern used in virtually
every real app.
"""

def contact_book():
    contacts = []  # list of dictionaries

    # Add contact to contact book
    def add_contact():
        name = input("Enter contact name: ")
        phone = input("Enter contact phone: ") 
        email = input("Enter contact email: ")
        contacts.append({'name': name, 'phone': phone, "email": email})
        print(f"Contact {name} added successfully.")

    # Search for contact
    def search_contact(name):
        for contact in contacts:
            if contact["name"].lower() == name.lower():
                return contact
        return None   # Returns None if contact not found

    # Delete contact
    def delete_contact(name):
        for i, contact in enumerate(contacts):
            if contact["name"].lower() == name.lower():
                del contacts[i]          
                print(f"Contact {name} deleted successfully.")
                return
        print(f"Contact {name} not found")

    # View all contacts
    def view_all():
        if not contacts:
            print("No contacts available.")
            return
        print("--- All Contacts in Contact_Book ---")
        print("-" * 66)

        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        print("-" * 66)

    # Main menu loop
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. View All Contacts")
        print("5. Exit")

        choice = input("Choose an option (1 - 5): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            name = input("Enter the name to search: ")
            result = search_contact(name)
            if result:
                print(f"Found contact - Name: {result['name']}, Phone: {result['phone']}, Email: {result['email']}")
            else:
                print(f"Contact {name} not found.")
        elif choice == '3':
            name = input("Enter the name to delete: ")
            delete_contact(name)
        elif choice == '4':
            view_all()
        elif choice == '5':
            print("Exit contact book. Bye")
            break
        else:
            print("Invalid option! Enter a number between 1 - 5.")

if __name__ == '__main__': #if name = main run contact (Run this file directly, not imported by another file)
    contact_book()