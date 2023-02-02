n = int(input())
max_snowball_snow = 0
max_snowball_time = 0
max_snowball_quality = 0
max_value = 0
for i in range(n):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_snow / snowball_time) ** snowball_quality

    if snowball_value > max_value:
        max_value = snowball_value
        max_snowball_snow = snowball_snow
        max_snowball_time = snowball_time
        max_snowball_quality = snowball_quality

print(f"{max_snowball_snow} : {max_snowball_time} = {max_value:.0f} ({max_snowball_quality})")
