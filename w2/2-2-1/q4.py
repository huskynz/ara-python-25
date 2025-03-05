# 1-1-1
# Peter
# peter@husky.nz
# wow

uword = input("Please enter a word whose letters are all lower case: ")

uwordu = input("Please enter a word whose letters are all upper case: ")

uwordcheck = uword.islower()
uworducheck = uwordu.isupper()


uwordchecklow = str(uwordcheck).lower()
uworduchecklow = str(uworducheck).lower()

print(f"It is {uwordchecklow} that {uword} is in all lower case letters.")
print(f"It is {uworduchecklow} that {uwordu} is in all upper case letters.")