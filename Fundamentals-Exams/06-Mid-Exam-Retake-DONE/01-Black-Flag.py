days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

gathered_plunder = 0
lost_plunder = 0
for day in range(1, days + 1):
    gathered_plunder += daily_plunder

    if day % 3 == 0:
        gathered_plunder += daily_plunder / 2

    if day % 5 == 0:
        lost_plunder = gathered_plunder * 0.3
        gathered_plunder -= lost_plunder

lost_percentage = 100 * (gathered_plunder / expected_plunder)
if gathered_plunder >= expected_plunder:
    print(f"Ahoy! {gathered_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {lost_percentage:.2f}% of the plunder.")