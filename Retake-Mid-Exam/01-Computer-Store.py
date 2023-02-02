total_sum_without_taxes = 0
taxes = 0
final_price = 0

while True:
    command = input()
    if command == "special":
        prices = float(command)
        total_sum_without_taxes += prices
        taxes = total_sum_without_taxes * 0.2
        final_price = total_sum_without_taxes + taxes

        if prices < 0:
            print("Invalid price!")
            continue

    if command == "special":
       final_price *= 0.1
       break


print(final_price)
