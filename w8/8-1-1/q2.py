# 1-1-1
# Peter
# peter@husky.nz
# wow

def validate_phone_number(area_code, extension_number, starting_digits):
    """
    THis works somehow, my code works somewhat
    """   
    # Convert inputs to strings
    area_code = str(area_code)
    extension_number = str(extension_number)
    
    # Validate starting_digits - all elements must be digits
    valid_starts = ''.join(map(str, starting_digits))
    if not valid_starts.isdigit():
        return (False,)
    
    # Validate area_code - must be exactly 3 digits
    if len(area_code) != 3 or not area_code.isdigit():
        return (False,)
        
    # Validate extension - must be exactly 4 digits and start with valid digit
    if len(extension_number) != 4 or not extension_number.isdigit():
        return (False,)
    
    # Check if extension starts with valid digit
    if extension_number[0] not in valid_starts:
        return (False,)
        
    # Return valid phone number
    return (True, area_code + extension_number)
