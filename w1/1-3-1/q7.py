# 1-1-1
# Peter
# peter@husky.nz
# wow


print("Meeting time calculator")


mhourstime = int(input("Please enter the start time (hours): "))

mminutesdtime = int(input("Please enter the start time (minutes): "))
                    
mdurationtime = int(input("Please enter the duration (minutes): "))

mminuts = mminutesdtime + mdurationtime%60

mhr = mhourstime + mdurationtime//60 + mminuts//60

mminutscor = mminuts%60

mhrcor = mhr%24

print()

print(f"The meeting will start at {mhourstime:0>2}:{mminutesdtime:0>2}")

print(f"The meeting will end at {mhrcor:0>2}:{mminutscor:0>2}")
