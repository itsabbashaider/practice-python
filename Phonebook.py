Phone_book = {}


def read_contact():
    name = input("Enter name: ")
    if name in Phone_book:
        print(f"{name}: {Phone_book[name]}")
    else:
        print("Contact does not exist")

def edit_contact():
    name = input("Enter the name for edit: ")
    if name in Phone_book:
        number = input("Enter the number for edit: ")
        Phone_book[name] = number
        print("Edited the Phone_book")
    else:
        print("Contact does not exist")

def delete_contact():
    name = input("Enter the name you want to delete: ")
    if name in Phone_book:
        del Phone_book[name]
        print("The contact is deleted")
    else:
        print("Contact does not exist")

def create_contact():
    name = input("Enter the name to create contact: ")
    if name in Phone_book:
        print("Contact already exist with this name")
    else:
        number = input("Enter the number for contact: ")
        Phone_book[name] = number
        print("Contact has been created")

def list_contacts():
    if not Phone_book:
        print("No contsct found")
    else:
        print("\nAll contacts")
        for name,number in Phone_book.items():
            print(f"{name}: {number}")
    

while True:
    print("0.Exit")
    print("1.Read")
    print("2.Edit")
    print("3.Delete")
    print("4.Create")
    print("5.List All")
   

    Action = input("Select your Action (0/1/2/3/4/5): ")

    if Action == '0':
        break
    if Action == '1':
        read_contact()
    elif Action == '2':
        edit_contact()
    elif Action == '3':
        delete_contact()
    elif Action == '4':
        create_contact()
    elif Action == '5':
        list_contacts()
    else:
        print("Invalid input")
