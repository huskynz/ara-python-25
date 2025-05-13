# 1-1-1
# Peter
# peter@husky.nz
# wow


# Dictionary to store contacts
contacts = {}

def display_as_list():
    """Displays the contacts as a list."""
    for name, number in contacts.items():
        print(f"{name:<15}: {number}")

def get_option():
    """Gets the user's menu option."""
    return input("Option: ").strip().upper()

def get_name():
    """Gets a contact name from the user."""
    return input("Contact: ").strip().title()

def get_number_as_string():
    """Gets a contact number from the user."""
    return input("Contact number: ").strip()  # For new contacts

def get_new_number():
    """Gets a new number for existing contact."""
    return input("New number: ").strip()  # For updates

def add_edit_contact():
    """Adds or edits a contact."""
    name = get_name()
    if name in contacts:
        print(f"{name} is already in the phone system.")
        update = input("Would you like to change the phone number? y/n: ").strip().lower()
        if update == 'y':
            new_number = get_new_number()  # Use new number prompt for updates
            if contacts[name] == new_number:
                print(f"{name} already has the number {new_number}. The number has not been changed.")
            else:
                contacts[name] = new_number
                print(f"{name} has been updated with the number: {new_number}.")
        else:
            print(f"{name} has not been updated.")
    else:
        number = get_number_as_string()  # Use contact number prompt for new contacts
        contacts[name] = number
        print(f"{name} has been added with the number: {number}.")

def remove_contact():
    """Removes a contact."""
    name = input("Enter the contact to be removed (or press Enter to cancel): ").strip().title()
    if name in contacts:
        del contacts[name]
        print(f"{name} has been removed from the contacts.")
    else:
        print(f"Sorry, {name} is not a contact.")

def show_contact():
    """Shows a specific contact."""
    name = get_name()
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"{name} is unknown.")

def display_contacts():
    """Displays all contacts."""
    if contacts:
        display_as_list()
    else:
        print("Sorry, there are no contacts.")

def empty_contacts():
    """Empties all contacts."""
    confirm = input("Please confirm that you want remove all the contacts.  y/n: ").strip().lower()
    if confirm == 'y':
        contacts.clear()
        print("All the contacts have been removed.")
    else:
        print("Contacts have not been removed.")

# Main menu loop
def main():
    running = True
    while running:
        print("\nTelephone contact options.")
        print("A) Add/edit a contact.")
        print("R) Remove a contact.")
        print("F) Find a contact.")
        print("D) Display all contacts.")
        print("E) Empty all contacts.")
        print("Q) Quit.")
        
        option = get_option()
        
        if option == 'A':
            add_edit_contact()
        elif option == 'R':
            remove_contact()
        elif option == 'F':
            show_contact()
        elif option == 'D':
            display_contacts()
        elif option == 'E':
            empty_contacts()
        elif option == 'Q':
            print("Bye.")
            running = False

# Run the program
if __name__ == "__main__":
    main()