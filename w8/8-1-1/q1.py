# 1-1-1
# Peter
# peter@husky.nz
# wow



def get_full_name(name_msg='Full name: '):
    """
    THis works somehow, my code works somewhat
    """
    full_name = input(name_msg)
    if not full_name.strip():
        return (False,)
    
    check_name = full_name.replace('-', '').replace('`', '').replace("'", '').replace(' ', '')
    if not check_name.isalpha():
        return (False,)
        
    name_parts = full_name.split()
    if len(name_parts) < 2:
        return (False,)
        
    return (True, [part.title() for part in name_parts])
