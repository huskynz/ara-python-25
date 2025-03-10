# 1-1-1
# Peter
# peter@husky.nz
# wow

fstartletter = "n"

fname = input("Please enter your first name: ")

fnamestrip = fname.strip()
fnamelower = fnamestrip.lower()
fnamecap = fnamelower.title()

fnameEndWith = fnamecap.endswith(fstartletter)

if fnameEndWith == True:
    print(f"Hi {fnamecap}, your first name ends with the letter {fstartletter}.")
else:
    print(f"Hi {fnamecap}, your first name does not end with the letter {fstartletter}.")