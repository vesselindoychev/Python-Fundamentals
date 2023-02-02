age = int(input())

DRINK = "drink"
TODDY = "toddy"
COKE = "coke"
BEER = "beer"
WHISKY = "whisky"

if age <= 14:
    print(f"{DRINK} toddy")
elif age <= 18:
    print(f"{DRINK} coke")
elif age <= 21:
    print(f"{DRINK} beer")
else:
    print(f"{DRINK} whisky")