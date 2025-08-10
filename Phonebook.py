Phone_book = {}
PHONE_BOOK_FILE = "Phonebook.txt" #Veriable for txt file .

def load_contacts():
    try:#try used for opening and reading the txt file.
        with open(PHONE_BOOK_FILE, "r") as file: #We call 'r' so we can read contacts from the txt file.
            for line in file: #Loop on every line of the txt file.
                name, number = line.strip().split(",")# Here we can remove all white spaces from L/R and separate them with comma (,).
                Phone_book[name] = number
    except FileNotFoundError: #If it gives FileNotFoundError problem the except method will run our code without breaking the code.
        pass #Used pass for indentation requirment.

def save_contacts():
    with open(PHONE_BOOK_FILE, "w") as file:#We call 'w' so we will be able to write anything in txt file.
        for name, number in Phone_book.items():#It loop though Phone_book and return name and number pairs.
            file.write(f"{name},{number}\n") #It write name and number pairs in new lines.


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
        save_contacts()#Call save function to save changes here.
        print("Edited the Phone_book")
    else:
        print("Contact does not exist")

def delete_contact():
    name = input("Enter the name you want to delete: ")
    if name in Phone_book:
        del Phone_book[name]
        save_contacts()#Call save function to save changes here.
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
        save_contacts()#Call save function to save changes here.
        print("Contact has been created")

def list_contacts():
    if not Phone_book:
        print("No contsct found")
    else:
        print("\nAll contacts")
        for name,number in Phone_book.items():
            print(f"{name}: {number}")
            
load_contacts()#Calling this function so while loop loads all the contacts from Phonebook.txt into the Phone_book dictionary.

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
    elif Action == '1':
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
#I made the changes syntax and the comments to understand what changes i made in the code.
#And used AI for some errors explaination.
