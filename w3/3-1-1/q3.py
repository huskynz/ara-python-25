# 1-1-1
# Peter
# peter@husky.nz
# wow
import re

fname = input("Please enter your first name: ")
fnamecapstrip = fname.title().strip()

regex = re.compile(r'[@_!#$%^&*.()<>?/\|}{~:]')

if(regex.search(fname) == None):
    print(f"{fnamecapstrip} is a valid name.")
else:
    print(f"{fnamecapstrip} is not a valid name.")
