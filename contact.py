import json

CONTACTS_FILE = "contacts.json"

def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email (optional): ").strip()

    if name in contacts:
        print("❌ Contact already exists!")
    else:
        contacts[name] = {"Phone": phone, "Email": email}
        save_contacts(contacts)
        print(f"✅ Contact '{name}' added successfully!")

def delete_contact(contacts):
    name = input("Enter contact name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"🗑️ Contact '{name}' deleted successfully!")
    else:
        print("❌ Contact not found!")

# Search for a contact
def search_contact(contacts):
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print(f"\n📞 Contact found:\nName: {name}\nPhone: {contacts[name]['Phone']}\nEmail: {contacts[name]['Email']}\n")
    else:
        print("❌ Contact not found!")

def view_contacts(contacts):
    if not contacts:
        print("📂 No contacts saved yet.")
    else:
        print("\n📜 Contact List:")
        for name, info in contacts.items():
            print(f"- {name}: {info['Phone']} ({info['Email']})")

def main():
    contacts = load_contacts()

    while True:
        print("\n📇 CONTACT MANAGER")
        print("1️⃣ Add Contact")
        print("2️⃣ Delete Contact")
        print("3️⃣ Search Contact")
        print("4️⃣ View All Contacts")
        print("5️⃣ Exit")

        choice = input("\nChoose an option (1-5): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            delete_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            view_contacts(contacts)
        elif choice == "5":
            print("👋 Exiting Contact Manager. Have a great day!")
            break
        else:
            print("❌ Invalid choice! Please select a valid option.")

main()