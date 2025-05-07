# 1-1-1
# Peter
# peter@husky.nz
# wow

def display_as_list(display_items,message=None,counter_reqd=None):
    """
    THis works somehow, my code works somewhat
    """
    if not display_items:
        print("Sorry, the list is empty.")
        return False
    else:
        print()
        
        for index, item in enumerate(display_items, start=1):
            if counter_reqd:
                print(f"{message} {index}: {item}")
            elif message == "Shopping item":
                print(f"Shopping item {index}: {item}")
            elif counter_reqd == None:
                print(f"Item {index}: {item} ")
            else:
                print(f"{item}")
        
        return True