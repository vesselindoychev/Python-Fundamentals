items = input().split("|")
budget = float(input())

prices_list = []

for cell in items:
    tokens = cell.split("->")
    item = tokens[0]
    price = float(tokens[1])

    if item == "Clothes" and price <= 50.0:
        prices_list.append(price)

    elif item == 'Shoes' and price <= 35.0:
        prices_list.append(price)

    elif item == "Accessories" and price <= 25.5:
        prices_list.append(price)

    else:
        continue
new_prices = []
res = []

for given_price in prices_list:
    profit = 0
    if budget >= given_price:
        budget -= given_price
        res.append(given_price)

    else:
        continue
total_sum = 0
for i in res:
    new_price = 0
    new_price += (i * 0.4) + i
    new_prices.append(f"{new_price:.2f}")


filtered_prices = list(map(float, new_prices))
profit = sum(filtered_prices) - sum(res)
print(" ".join(new_prices))
print(f"Profit: {profit:.2f}")

if budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")