# 1-1-1
# Peter
# peter@husky.nz
# wow

fname=input("Please enter your first name: ")

fnamestrip=fname.strip()
fnamecap= fnamestrip.capitalize()

lname=input(f"{fnamecap}, please enter your last name: ")

lnamestrip=lname.strip()
lnamecap=lnamestrip.capitalize()


umess=input(f"{fnamecap}, please enter a message: ")

umessstrip=umess.strip()

cstart=int(input("Please enter the start position: "))
cend=int(input("Please enter the end position: "))

cstartfix=cstart - 1

usencnt=len(umessstrip)

usechc=umessstrip[cstartfix:cend]

print(f"Report for {fnamecap + ' ' + lnamecap}'s sentence of {usencnt} characters.")

print(f"The characters '{usechc}' can be found in position {cstart} to position {cend} inclusively.")