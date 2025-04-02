# 1-1-1
# Peter
# peter@husky.nz
# wow

def add_item(user_list):
    """
    THis works somehow, my code works somewhat
    """
    itemin = input("Please enter the item to be added: ")

    item = itemin.strip().lower().capitalize

    return_value = item

    if item == " ":
        print("No item was entered.")
        return False
    elif item in user_list:
        uchoice=input(f"[{item}] is already in the list, please confirm that you want to add another (y/n): ")
        if uchoice == "y":
            return return_value
        elif uchoice == "n":
            print(f"[{item}] was not added.")
        else:
           return return_value


items = ['One','Two']
return_value = add_item(items)
print(items)