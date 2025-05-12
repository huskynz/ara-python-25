
from q3 import get_name
from q4 import get_number_as_string

def add_edit_contact(contacts):
    """
    Adds a new contact or edits an existing one in the contacts dictionary.
    Returns True if a contact was added or updated, otherwise returns False.
    """
    name = get_name()
    print(f"Contact: {name}")
    formatted_name = name.title()

    if formatted_name not in contacts:
        number = get_number_as_string("Contact number: ", 3)
        contacts[formatted_name] = number
        print(f"{formatted_name} has been added with the number: {number}.")
        return True
    else:
        print(f"{formatted_name} is already in the phone system.")
        option = get_option("Would you like to change the phone number? y/n: ")
        if option.lower() == 'y':
            new_number = get_number_as_string("New number: ", 3)
            if contacts[formatted_name] != new_number:
                contacts[formatted_name] = new_number
                print(f"{formatted_name} has been updated with the number: {new_number}.")
                return True
            else:
                print(f"{formatted_name} already has the number {new_number}. The number has not been changed.")
                return False
        else:
            print(f"{formatted_name} has not been updated.")
            return False

