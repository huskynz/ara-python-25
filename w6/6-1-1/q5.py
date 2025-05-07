# 1-1-1
# Peter
# peter@husky.nz
# wow

def add_item(user_list):
<<<<<<< HEAD
    """
    THis works somehow, my code works somewhat
    """
    itemin = input("Please enter the item to be added: ")

    item = itemin.strip().lower().capitalize()

    return_value = item
=======
    """Add an item to the shopping list with validation."""
>>>>>>> 039f9b31f2d189892b13511e503e43187d64f06f

    if item == " ":
        print("No item was entered.")
<<<<<<< HEAD
        return False
    elif item in user_list:
        uchoice=input(f"[{item}] is already in the list, please confirm that you want to add another (y/n): ")
        if uchoice == "y":
            return return_value
        elif uchoice == "n":
            print(f"[{item}] was not added.")
        else:
           return return_value


=======
        print(f"{get_total_items(user_list)}")
        return False
        
    # Check if item already exists
    if item in user_list:
        if get_option(f"[{item}] is already in the list. Do you want to add another? (y/n): ") == 'y':
            user_list.append(item)
            print(f"[{item}] was added to the list.")
            print(f"{get_total_items(user_list)}")
            return True
        else:
            print(f"[{item}] was not added.")
            print(f"{get_total_items(user_list)}")
            return False
            
    # Add new item
    user_list.append(item)
    print(f"[{item}] was added to the list.")
    print(f"{get_total_items(user_list)}")
    return True
>>>>>>> 039f9b31f2d189892b13511e503e43187d64f06f






shop_items = []
return_value = add_item(shop_items)
print(f'The function returned: {return_value}')
print(shop_items)

# Test for no item being entered.
# The enter key was pressed.
return_value = add_item(shop_items)
print(f'The function returned: {return_value}')
print(shop_items)

# Add an item to the list
return_value = add_item(shop_items)
print(f'The function returned: {return_value}')
print(shop_items)