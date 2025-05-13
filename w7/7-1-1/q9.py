# 1-1-1
# Peter
# peter@husky.nz
# wow

def empty_contacts(contacts):
    """
    THis works somehow, my code works somewhat
    """   

    if not contacts:
        print("Sorry, there are no contacts.")
        return False
    
    user_input = get_option("Please confirm that you want remove all the contacts. y/n: ")
    
    if user_input.lower() == 'y':
        contacts.clear()
        print("All the contacts have been removed.")
        return True
    elif user_input.lower() == 'n':
        print("The contacts have not been removed.")
        return False
    else:
        print("Yikes, please don't empty the contacts!")
        return False