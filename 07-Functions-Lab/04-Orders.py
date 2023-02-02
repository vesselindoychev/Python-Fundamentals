def orders(product, quantity):
    price = None
    if product == "coffee":
        price = 1.5

    if product == "water":
        price = 1

    if product == "coke":
        price = 1.4

    if product == "snacks":
        price = 2

    total_price = price * quantity
    return (f"{total_price:.2f}")


product = input()
quantity = int(input())
print(orders(product, quantity))
