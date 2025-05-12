# 1-1-1
# Peter
# peter@husky.nz
# wow
def display_contacts(contacts):
    """
    THis works somehow, my code works somewhat
    """   
    if contacts:
        for name, phone in contacts.items():
            print(f"{name:<15}: {phone}")
        return True
    else:
        print("Sorry, there are no contacts.")
        return False