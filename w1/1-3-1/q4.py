# 1-1-1
# Peter
# peter@husky.nz
# wow


usr_name = input("Please enter your first name: ")

ex_rate = input(f"Hi {usr_name}. Please enter the NZ/AU exchange rate: ")

usr_amount = float(input("Please enter the amount of NZ $'s you want to exchange: "))

ex_amount = float(usr_amount) * float(ex_rate)

print(f"{usr_name}, I can exchange NZ ${usr_amount:.2f} into AU ${ex_amount:.2f} for you.")