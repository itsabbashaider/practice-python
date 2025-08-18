def load_contacts(phone_book_file_path,contacts_dict):
    try:  # try used for opening and reading the txt file.
        with open(phone_book_file_path, "r") as file:  # We call 'r' so we can read contacts from the txt file.
            for line in file:  # Loop on every line of the txt file.
                name, number = line.strip().split(",")  # Here we can remove all white spaces from L/R and separate them with comma (,).
                contacts_dict[name] = number
    except FileNotFoundError:  # If it gives FileNotFoundError problem the except method will run our code without breaking the code.
        print("File was not found")

def save_contacts(phone_book_file_path,contacts_dict):
    with open(phone_book_file_path, "w") as file:  # We call 'w' so we will be able to write anything in txt file.
        for name, number in contacts_dict.items():  # It loop though phone_book and return name and number pairs.
            file.write(f"{name},{number}\n")  # It write name and number pairs in new lines.


def read_contact(contacts_dict):
    name = input("Enter name: ")
    if name in contacts_dict:
        print(f"{name}: {contacts_dict[name]}")
    else:
        print("Contact does not exist")

def edit_contact(phone_book_file_path,contacts_dict):
    name = input("Enter the name for edit: ")
    if name in contacts_dict:
        number = input("Enter the number for edit: ")
        contacts_dict[name] = number
        save_contacts(phone_book_file_path,contacts_dict)  # Call save function to save changes here.
        print("Edited the phone_book")
    else:
        print("Contact does not exist")

def delete_contact(phone_book_file_path,contacts_dict):
    name = input("Enter the name you want to delete: ")
    if name in contacts_dict:
        del contacts_dict[name]
        save_contacts(phone_book_file_path,contacts_dict)  # Call save function to save changes here.
        print("The contact is deleted")
    else:
        print("Contact does not exist")

def create_contact(phone_book_file_path,contacts_dict):
    name = input("Enter the name to create contact: ")
    if name in contacts_dict:
        print("Contact already exist with this name")
    else:
        number = input("Enter the number for contact: ")
        contacts_dict[name] = number
        save_contacts(phone_book_file_path,contacts_dict)  # Call save function to save changes here.
        print("Contact has been created")

def list_contacts(contacts_dict):
    if not contacts_dict:
        print("No contsct found")
    else:
        print("\nAll contacts")
        for name,number in contacts_dict.items():
            print(f"{name}: {number}")

def main():   
    PHONE_BOOK_FILE = "Phonebook.txt"  # Veriable for txt file .
    phone_book = {}
    load_contacts(PHONE_BOOK_FILE,phone_book)  # Calling this function so while loop loads all the contacts from Phonebook.txt into the phone_book dictionary.

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
            read_contact(phone_book)
        elif Action == '2':
            edit_contact(PHONE_BOOK_FILE,phone_book)
        elif Action == '3':
            delete_contact(PHONE_BOOK_FILE,phone_book)
        elif Action == '4':
            create_contact(PHONE_BOOK_FILE,phone_book)
        elif Action == '5':
            list_contacts(phone_book)
        else:
            print("Invalid input")
            
if __name__ == '__main__':
    main()

