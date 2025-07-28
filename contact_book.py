# Contact Book CLI using Core Python

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    tags = input("Enter tags (comma-separated): ").split(',')
    contacts[name] = {
        "phone": phone,
        "email": email,
        "tags": set(tag.strip() for tag in tags)
    }
    print(f"\n✅ {name} added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts to display.")
    else:
        for name, info in contacts.items():
            print(f"\n👤 Name: {name}")
            print(f"📞 Phone: {info['phone']}")
            print(f"📧 Email: {info['email']}")
            print(f"🏷️ Tags: {', '.join(info['tags'])}")

def search_contact(contacts):
    name = input("Enter name to search: ")
    if name in contacts:
        info = contacts[name]
        print(f"\n👀 Contact Found!")
        print(f"📞 Phone: {info['phone']}")
        print(f"📧 Email: {info['email']}")
        print(f"🏷️ Tags: {', '.join(info['tags'])}")
    else:
        print("❌ Contact not found!")

def edit_contact(contacts):
    name = input("Enter name to edit: ")
    if name in contacts:
        print("Leave blank to keep existing value.")
        phone = input("New phone (optional): ")
        email = input("New email (optional): ")
        tags = input("New tags (comma-separated): ")

        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email
        if tags:
            contacts[name]["tags"] = set(tag.strip() for tag in tags.split(','))
        print(f"✅ {name} updated successfully!")
    else:
        print("❌ Contact not found!")

def delete_contact(contacts):
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"🗑️ {name} deleted successfully!")
    else:
        print("❌ Contact not found!")

def contact_book():
    contacts = {}
    while True:
        print("\n📒 Contact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            edit_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again!")

# Run the app
contact_book()
