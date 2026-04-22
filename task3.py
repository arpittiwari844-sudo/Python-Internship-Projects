contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    contact = {"name": name, "phone": phone}
    contacts.append(contact)

    print("Contact added successfully ✅")


def view_contacts():
    if not contacts:
        print("No contacts found ❌")
    else:
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")


def search_contact():
    name = input("Enter name to search: ")

    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("Contact found ✅")
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
            return

    print("Contact not found ❌")


def delete_contact():
    name = input("Enter name to delete: ")

    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted ✅")
            return

    print("Contact not found ❌")


while True:
    print("\nContact Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Goodbye 👋")
        break
    else:
        print("Invalid choice ❌")