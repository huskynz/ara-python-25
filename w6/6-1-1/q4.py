# 1-1-1
# Peter
# peter@husky.nz
# wow

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