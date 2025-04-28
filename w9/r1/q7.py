# 1-1-1
# Peter
# peter@husky.nz
# wow

fendletter = "n"

fname = input("Please enter your first name: ")

fnamestrip = fname.strip().lower()
fnamecap = fnamestrip.title()

fnameEnd = fnamecap.endswith(fendletter)

if fnameEnd == True:
    print(f"Hi {fnamecap}, your first name ends with the letter {fendletter}.")
else:
    print(f"Hi {fnamecap}, your first name does not end with the letter {fendletter}.")