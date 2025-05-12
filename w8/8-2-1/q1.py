def load_user_data(file_name):
    """
    Reads user data from a file and returns it as a dictionary.
    """
    with open(file_name, 'r') as file:
        line = file.read()
        
    return {
        'Initial': line[0],
        'LastName': line[1:-2],
        'Age': line[-2:]
    }