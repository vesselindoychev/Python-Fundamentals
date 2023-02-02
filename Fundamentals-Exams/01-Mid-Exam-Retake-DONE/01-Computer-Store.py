taxes = 0
price_without_taxes = 0
total_price = 0
while True:
    command = input()

    if command == "regular" or command == "special":
        break

    price = float(command)

    if price < 0:
        print("Invalid price!")
        continue
    price_without_taxes += price
    taxes = price_without_taxes * 0.2
    total_price = price_without_taxes + taxes


if command == "special":
    total_price *= 0.9
    if total_price == 0:
        print("Invalid order!")
    else:
        print(f"Congratulations you've just bought a new computer!\n"
              f"Price without taxes: {price_without_taxes:.2f}$\n"
              f"Taxes: {taxes:.2f}$\n"
              f"-----------\n"
              f"Total price: {total_price:.2f}$")

else:
    if total_price == 0:
        print("Invalid order!")
    else:
        print(f"Congratulations you've just bought a new computer!\n"
              f"Price without taxes: {price_without_taxes:.2f}$\n"
              f"Taxes: {taxes:.2f}$\n"
              f"-----------\n"
              f"Total price: {total_price:.2f}$")

