# 1. Add contact
# 2. View all contacts
# 3. Search contact
# 4. Delete contact
# 5. Quit
# Choose an option: 1
# Name: Ada
# Phone: 0801234567
# Email: ada@email.com
# Contact added!

# Choose an option: 3
# Search name: Ada
# Found: Ada, 0801234567, ada@email.com

# Choose an option: 5
# Goodbye!

contacts = []

print("1. Add contact")
print("2. View all contacts")
print("3. Search contact")
print("4. Delete contact")
print("5. Quit")

while True:
    data = int(input("Enter the a number from the options: "))
    if data == 1:
        name = input("Enter the name of contact: ")
        phone = input("Enter the phone number: ")
        email = input("Enter the email address: ")

        contact = {
            'Name': name,
            'Phone': phone,
            'Email': email
        }
        contacts.append(contact)
        print("Contact added!")
    elif data == 2:
        for contact in contacts:
            print(f"Name: {contact['Name']}")
            print(f"Phone: {contact['Phone']}")
            print(f"Email: {contact['Email']}")
            print()
    elif data == 3:
        search = input("Enter contact name to search: ")
        found = False
        for contact in contacts:
            if contact['Name'] == search:
                print(contact)
                found = True
        if not found:
            print("Contact not found")
    elif data == 4:
        delete = input("Enter contact to del: ")
        found = False
        for contact in contacts:
            if contact['Name'] == delete:
                contacts.remove(contact)
                print("Contact deleted!")
                found = True
                break
        if not found:
            print("Contact not found!")
    elif data == 5:
        print("Goodbye!")
        break
    else:
        print("Invalid input")
        print("Pick a number from 1-5")


