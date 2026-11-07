contacts = {
    "Anita": {
        "phones": ["9876543210"],
        "email": "anita@mail.com",
        "city": "Pune"
    },
    "Manoj": {
        "phones": ["9123456780", "9988776655"],
        "email": "manoj@mail.com",
        "city": "Delhi"
    },
    "Zara": {
        "phones": ["9000011111"],
        "email": "zara@mail.com",
        "city": "Pune"
    }
}


def valid_phone(phone):

    return phone.isdigit() and len(phone) == 10


def phone_exists(phone):

    for data in contacts.values():

        if phone in data["phones"]:
            return True

    return False


def add_contact():

    name = input("Enter contact name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    if name in contacts:
        print("Contact already exists.")
        return

    phone = input("Enter phone number: ").strip()

    if not valid_phone(phone):
        print("Phone number must contain exactly 10 digits.")
        return

    if phone_exists(phone):
        print("This phone number already belongs to another contact.")
        return

    email = input("Enter email: ").strip()
    city = input("Enter city: ").strip()

    contacts[name] = {
        "phones": [phone],
        "email": email,
        "city": city
    }

    print("Contact added successfully.")


def add_phone():

    name = input("Enter contact name: ").strip()

    if name not in contacts:
        print("Contact not found.")
        return

    phone = input("Enter additional phone number: ").strip()

    if not valid_phone(phone):
        print("Phone number must contain exactly 10 digits.")
        return

    if phone_exists(phone):
        print("This phone number is already registered.")
        return

    contacts[name]["phones"].append(phone)

    print("Phone number added successfully.")


def update_contact():

    name = input("Enter contact name: ").strip()

    if name not in contacts:
        print("Contact not found.")
        return

    print("1. Update Email")
    print("2. Update City")

    choice = input("Enter your choice: ")

    if choice == "1":

        email = input("Enter new email: ").strip()
        contacts[name]["email"] = email

        print("Email updated successfully.")

    elif choice == "2":

        city = input("Enter new city: ").strip()
        contacts[name]["city"] = city

        print("City updated successfully.")

    else:
        print("Invalid choice.")


def delete_contact():

    name = input("Enter contact name: ").strip()

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


def search_contact():

    search_name = input("Enter name to search: ").strip().lower()

    found = False

    for name, data in contacts.items():

        if search_name in name.lower():

            print("\nName:", name)
            print("Phone Numbers:", data["phones"])
            print("Email:", data["email"])
            print("City:", data["city"])

            found = True

    if not found:
        print("No matching contact found.")


def reverse_lookup():

    reverse = {}

    for name, data in contacts.items():

        for phone in data["phones"]:
            reverse[phone] = name

    phone = input("Enter phone number: ").strip()

    if phone in reverse:
        print("Contact Name:", reverse[phone])
    else:
        print("Phone number not found.")


def reports():

    # Group contacts by city
    city_groups = {}

    for name, data in contacts.items():

        city = data["city"]

        city_groups.setdefault(city, []).append(name)

    print("\n1. Contacts Grouped by City")

    for city, names in city_groups.items():
        print(city, ":", names)

    # Find contacts with multiple phone numbers
    print("\n2. Contacts with Multiple Phone Numbers")

    found = False

    for name, data in contacts.items():

        if len(data["phones"]) > 1:
            print(name, ":", data["phones"])
            found = True

    if not found:
        print("No contacts with multiple numbers.")

    # Display contacts alphabetically
    print("\n3. Complete Phone Directory")

    for name in sorted(contacts):

        data = contacts[name]

        print("\nName:", name)
        print("Phone:", data["phones"])
        print("Email:", data["email"])
        print("City:", data["city"])


while True:

    print("\n===== PHONE DIRECTORY =====")
    print("1. Add Contact")
    print("2. Add Another Phone Number")
    print("3. Update Email or City")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Reverse Phone Lookup")
    print("7. Reports")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        add_phone()

    elif choice == "3":
        update_contact()

    elif choice == "4":
        delete_contact()

    elif choice == "5":
        search_contact()

    elif choice == "6":
        reverse_lookup()

    elif choice == "7":
        reports()

    elif choice == "8":
        print("Exiting Phone Directory.")
        break

    else:
        print("Invalid choice. Try again.")