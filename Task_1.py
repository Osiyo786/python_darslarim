import math
raeding=float(input("Reading [1-10]:"))
speaking=float(input("Speaking [1-10]:"))
listening= float(input("Listening [1-10]:"))
writing=float(input("Writing [1-10]:"))
result=round((raeding+speaking+listening+writing)/4)
if raeding == 10 or speaking == 10 or listening == 10 or writing == 10:
    print("Siz bu bo'limlardan 10 bal ololmaysiz!")
else:
    if 3 <= result <= 5:
        money = 1000000

    elif 6 <= result <= 8:
        money = 1000000

    elif 9 <= result > 10:
        money = 5000000
    print(f"Sizning jami to'plagan balingiz {result}")
    print(f"Siz qo'lga kiritgan mablag' {money}")
