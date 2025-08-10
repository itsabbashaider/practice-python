Phonebook = {"Abbas"    : 317,
             "Haider"   : 318,
             "Ali"      : 319,
             "Muhammad" : 320}


def read_contact():
    name = input("Enter name: ")
    if name in Phonebook:
        print(f"{name}: {Phonebook[name]}")
    else:
        print("Contact does not exist")

def edit_contact():
    name = input("Enter the name for edit: ")
    if name in Phonebook:
        number = input("Enter the number for edit: ")
        Phonebook[name] = number
        print("Edited the Phonebook")
    else:
        print("Contact does not exist")
def delete_contact():
    name = input("Enter the name you want to delete: ")
    if name in Phonebook:
        del Phonebook[name]
        print("The contact is deleted")
    else:
        print("Contact does not exist")
def create_contact():
    name = input("Enter the name to create contact: ")
    if name in Phonebook:
        print("Contact already exist with this name")
    else:
        number = input("Enter the number for contact: ")
        Phonebook[name] = number
        print("Contact has been created")
def list_contacts():
    if not Phonebook:
        print("No contsct found")
    else:
        print("\nAll contacts")
        for name,number in Phonebook.items():
            print(f"{name}: {number}")
    
exit_key = "Q"

while True:
    print("1.Read")
    print("2.Edit")
    print("3.Delete")
    print("4.Create")
    print("5.List All")


    Action = input("Select your Action (1/2/3/4/5): ")


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
    exit_key = (input(f"If you want to exit  ({exit_key}): "))
    if "Q" in exit_key :
         break