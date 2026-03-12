# Contact Book 

contacts = {}

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. Edit Contact")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. View All Contacts")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            try:
                name = input("Enter name: ")
                phone = input("Enter phone number: ")

                if name == "" or phone == "":
                    raise ValueError("Fields cannot be empty")

                if name in contacts:
                    raise KeyError("Contact already exists")

                if not phone.isdigit() or len(phone) != 10:
                    raise ValueError("Phone number must be 10 digits")

                contacts[name] = phone
                print("Contact saved successfully")

            except (ValueError, KeyError) as e:
                print("Error:", e)

        elif choice == 2:
            try:
                name = input("Enter name to edit: ")

                if name not in contacts:
                    raise KeyError("Contact not found")

                phone = input("Enter new phone number: ")

                if not phone.isdigit() or len(phone) != 10:
                    raise ValueError("Invalid phone number")

                contacts[name] = phone
                print("Contact updated")

            except (ValueError, KeyError) as e:
                print("Error:", e)

        elif choice == 3:
            name = input("Enter name to search: ")

            if name in contacts:
                print("Name:", name)
                print("Phone:", contacts[name])
            else:
                print("Contact not found")

        elif choice == 4:
            try:
                name = input("Enter name to delete: ")

                if name not in contacts:
                    raise KeyError("Contact not found")

                del contacts[name]
                print("Contact deleted")

            except KeyError as e:
                print("Error:", e)

        elif choice == 5:
            if len(contacts) == 0:
                print("No contacts saved")
            else:
                for i in contacts:
                    print(i, ":", contacts[i])

        elif choice == 6:
            print("Exiting...")
            break

        else:
            print("Invalid choice")

    except ValueError:
        print("Please enter a valid number")