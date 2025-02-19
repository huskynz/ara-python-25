# 1-1-1
# Peter
# peter@husky.nz
# wow
import math

usrfname = input("Please enter your first name: ")

print(f"Hi {usrfname}.")

usrfint = int(input("Please enter the first integer: "))
usrlint = int(input("Please enter the second integer: "))

usranswer = usrfint
usranswer /= usrlint

usrout = math.trunc(usranswer)

usrremaind = usrfint % usrlint


print(f"{usrfname}, the answer to {usrfint} divided by {usrlint} is {usrout} with a remainder of {usrremaind}.")