collection = input().split("|")
budget = float(input())


TICKETS = 150

str_new_prices = 0
price_list = []
profit = 0
sum_of_new_prices = 0
money_for_ticket = 0
new_price = 0
new_prices = []
renew_price_list = []

for cell in collection:
    tokens = cell.split("->")

    outfit = tokens[0]
    price = float(tokens[1])

    if outfit == "Clothes" and price <= 50.00:
        price_list.append(price)

    elif outfit == "Shoes" and price <= 35.00:
        price_list.append(price)

    elif outfit == "Accessories" and price <= 20.50:
        price_list.append(price)

    else:
        continue


for j in price_list:
    if budget >= j:
        budget -= j
        new_price = j + j * 0.4

        sum_of_new_prices += j + (j * 0.4)
        new_prices.append(f"{new_price:.2f}")
        renew_price_list.append(j)
    else:
        continue

profit = sum_of_new_prices - sum(renew_price_list)
money_for_ticket = budget + sum_of_new_prices


print(" ".join(new_prices))
print(f"Profit: {profit:.2f}")
if money_for_ticket >= TICKETS:
    print("Hello, France!")
else:
    print("Time to go.")