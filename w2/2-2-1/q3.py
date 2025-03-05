# 1-1-1
# Peter
# peter@husky.nz
# wow

uword = input("Please enter a word that starts with a capital letter and with subsequent letters in lower case: ")

uwordcheck = uword[0].isupper()

uwordchecklow = str(uwordcheck).lower()

print(f"It is {uwordchecklow} that {uword} starts with a capital letter and all subsequent letters are in lower case.")