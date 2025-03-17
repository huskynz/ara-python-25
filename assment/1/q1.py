# 1-1-1
# Peter
# peter@husky.nz
# wow

beachtoday = int(input("Please enter the temperature: "))
DayOfWeek = input("Please enter the day: ")

DayOfWeekStrip = DayOfWeek.strip()


DayOfWeekLower = DayOfWeekStrip.lower()

beachtodayover25 = beachtoday >= 25

beachtodayunder30 = beachtoday <= 30

vaildbeachday = beachtodayover25 is True and beachtodayunder30 is True and DayOfWeekLower == "sunday" or DayOfWeekLower == "saturday"
vaildbeachdaylow = str(vaildbeachday).lower()

if vaildbeachday == True:
    print("Let's go to the beach!")
else:
    print("No beach today!")