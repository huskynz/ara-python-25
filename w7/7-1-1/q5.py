# 1-1-1
# Peter
# peter@husky.nz
# wow

def get_name(message="Contact: "):
    """
    THis works somehow, my code works somewhat
    """
    umess = input(f"{message}")
    return umess.lower().strip().title()

def get_number_as_string(message, min_length):
    """
    THis works somehow, my code works somewhat
    """
    while True:
        user_input = input(message).replace(" ","")

        if not user_input.isdigit():
          print("Digits only please.")
        elif len(user_input) < min_length:
           print(f"The number must be at least {min_length} digits long.")
        else:
           return user_input  

def add_edit_contact(contacts):
    """
    THis works somehow, my code works somewhat
    """
    contact_name = get_name("Enter contact name: ")
    
        # If contact is not in the dictionary, add the new contact with their number.
    if contact_name not in contacts:
        # Ensure get_number_as_string returns a valid number
        phone_number = get_number_as_string('Contact number: ', 3)
        
        # Add the new contact with their phone number
        contacts[contact_name] = phone_number
        print(f"Contact: {contact_name}")
        print(f"{contact_name} has been added with the number: {phone_number}.")
        return True
    
    else:
        # If the contact exists, ask if the user wants to change the number.
        print(f"Contact: {contact_name}")
        print(f"{contact_name} is already in the phone system.")
        
        # Check if the user wants to update the phone number
        if get_option('Would you like to change the phone number? y/n: ').lower() == 'y':
            # Get the new phone number
            new_number = get_number_as_string('New number: ', 3)
            
            # If the new number is different from the existing one, update it
            if new_number != contacts[contact_name]:
                contacts[contact_name] = new_number
                print(f"{contact_name} has been updated with the number: {new_number}.")
                return True
            else:
                print(f"{contact_name} already has the number {new_number}. The number has not been changed.")
                return False
        else:
            # User chose not to update the contact
            print(f"{contact_name} has not been updated.")
            return False
def add_edit_contact(contacts):
    """
    THis works somehow, my code works somewhat
    """
    # Get the contact name and number from the user
    contact_name = get_name("Enter contact name: ")

    # Case 1: Add new contact if not already in the dictionary
    if contact_name not in contacts:
        phone_number = get_number_as_string('Contact number: ', 3)
        contacts[contact_name] = phone_number
        print(f"Contact: {contact_name}")
        print(f"{contact_name} has been added with the number: {phone_number}.")
        return True

    # Case 2: Modify existing contact if already in the dictionary
    else:
        print(f"Contact: {contact_name}")
        print(f"{contact_name} is already in the phone system.")
        
        # Ask if they want to change the number
        option = get_option('Would you like to change the phone number? y/n: ').lower()

        if option == 'y':
            new_number = get_number_as_string('New number: ', 3)
            
            # Check if the new number is different from the old one
            if new_number != contacts[contact_name]:
                contacts[contact_name] = new_number
                print(f"{contact_name} has been updated with the number: {new_number}.")
                return True
            else:
                print(f"{contact_name} already has the number {new_number}. The number has not been changed.")
                return False
        else:
            print(f"{contact_name} has not been updated.")
            return False

# Add new contact
# Test parameter name
personal_contacts = {'Ms One':'101',
                    'Mr Two':'102',
                    'Ms Tree':'103'
                    }
modification_status = add_edit_contact(contacts=personal_contacts)
print(personal_contacts)