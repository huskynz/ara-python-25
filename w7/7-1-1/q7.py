# 1-1-1
# Peter
# peter@husky.nz
# wow

def show_contact(contacts):
    """
    THis works somehow, my code works somewhat
    """
    contact_name = get_name("Contact: ")
    contact_name_formatted = contact_name.title()

    if contact_name_formatted in contacts:
        print(f"{contact_name_formatted}: {contacts[contact_name_formatted]}")
        return True
    else:
        print(f"{contact_name_formatted} is unknown.")
        return False