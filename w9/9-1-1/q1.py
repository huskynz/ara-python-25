# The strings below need to be added to the code.  Do not alter anything inside the quotes.
# 'An error occurred while attempting to create the dir.'
# 'An error occurred while attempting to delete the dir.'


# Program code that needs to be modified:

# Lab 9-1-1 Q1 Dr. Amit Sarkar
 
import os

def create_dir():
    """Create a directory. Return resulting message."""
    
    dir_name = get_dir_name(CREATE_ACTION)
    try:
        # Let's try to create it
        os.mkdir(dir_name)
        return f'{dir_name} has been created.'
    except:
        return 'An error occurred while attempting to create the dir.'


def remove_dir():
    """ Remove a directory.  Return resulting message."""
    
    dir_name = get_dir_name(REMOVE_ACTION)
    try:
        # Let's try to remove it
        os.rmdir(dir_name)
        return f'{dir_name} has been removed.'
    except:
        return 'An error occurred while attempting to delete the dir.'


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

    
def get_option(prompt_msg="Option: "):
    """
    THis works somehow, my code works somewhat
    """
    umess = input(f"{prompt_msg}")
    return umess.lower().strip()


def get_dir_name(action):
    """ Return the entered directory name. """
    
    return input(f'Please enter the name of the directory to be {action}: ').strip()


# Initialise objects
CREATE_DIR_OPTION = 'c'
REMOVE_DIR_OPTION = 'r'
EXIT_OPTION = 'e'
CREATE_ACTION = 'created'
REMOVE_ACTION = 'removed'

MENU = ('Please enter one of the following options:',
        'C) Create a directory.',
        'R) Remove a directory.',
        'E) Exit'
        )
        
option = '' 

while option != EXIT_OPTION:

    display_as_list(MENU, counter_reqd=False)
      
    option = get_option() 
 
    if option == CREATE_DIR_OPTION:
        msg = create_dir()
        print(msg)

    elif option == REMOVE_DIR_OPTION:
        msg = remove_dir()
        print(msg)
         
print('Bye.')
