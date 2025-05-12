# 1-1-1
# Peter
# peter@husky.nz
# wow


def remove_contact(contacts):
    """
    THis works somehow, my code works somewhat
    """
    if not contacts:
        print("Sorry, there are no contacts.")
        return False
    
    contact_to_remove = get_name('Enter the contact to be removed (or press Enter to cancel): ')
    
    if contact_to_remove == '':
        print("Cancelling the remove request.")
        return False
    
    if contact_to_remove in contacts:
        del contacts[contact_to_remove]
        print(f"{contact_to_remove} has been removed from the contacts.")
        return True
    
    print(f"Sorry, {contact_to_remove} is not a contact.")
    return False
