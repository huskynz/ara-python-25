# 1-1-1
# Peter
# peter@husky.nz
# wow

fstartletter = "A"

fname = input("Please enter your first name: ")

fnamestrip = fname.strip()
fnamecap = fnamestrip.capitalize()

fnameStartWithA = fnamecap.startswith(fstartletter)

if fnameStartWithA == True:
    print(f"Hi {fnamecap}, your first name starts with the letter {fstartletter}.")
else:
    print(f"Hi {fnamecap}, your first name does not start with the letter {fstartletter}.")