# 1-1-1
# Peter
# peter@husky.nz
# wow

#def add_item(user_list):
#    """
#    THis works somehow, my code works somewhat
#    """
#    itemin = input("Please enter the item to be added: ")
#
#    item = itemin.strip().lower().capitalize()
#
#    return_value = item
#
#    if item == " ":
#        print("No item was entered.")
#        return False
#    elif item in user_list:
#        uchoice=input(f"[{item}] is already in the list, please confirm that you want to add another (y/n): ")
#        if uchoice == "y":
#            return return_value
#        elif uchoice == "n":
#            print(f"[{item}] was not added.")
#        else:
#           return return_value
#


def add_item(user_list):
    """Add an item to the shopping list with validation."""
    def get_item(prompt_msg="Item: "):
        umess = input(f"{prompt_msg}")
        return umess.lower().strip().capitalize()
    def get_total_items(user_list):
        """
        THis works somehow, my code works somewhat
        """
        msglen = len(user_list)

        phrase = "1) Onwards and upwards."

        if phrase in user_list:
            return f"There is {msglen} item in the list."
        else: 
            return f"There are {msglen} items in the list."

    # Get the item from user
    item = get_item()
    
    # Handle empty input
    if not item:
        print("No item was entered.")
        print(f"Total items in the list: {get_total_items(user_list)}")
        return False
        
    # Check if item already exists
    if item in user_list:
        if get_option(f"[{item}] is already in the list. Do you want to add another? (y/n): ") == 'y':
            user_list.append(item)
            print(f"[{item}] was added to the list.")
            print(f"Total items in the list: {get_total_items(user_list)}")
            return True
        else:
            print(f"[{item}] was not added.")
            print(f"Total items in the list: {get_total_items(user_list)}")
            return False
            
    # Add new item
    user_list.append(item)
    print(f"[{item}] was added to the list.")
    print(f"Total items in the list: {get_total_items(user_list)}")
    return True

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