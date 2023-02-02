budget = float(input())
one_kg_flour_price = float(input())

pack_of_eggs = 0.75 * one_kg_flour_price
one_liter_milk_price = 1.25 * one_kg_flour_price
milk_price_for_cozonac = one_liter_milk_price / 4

cozonac_price = pack_of_eggs + one_kg_flour_price + milk_price_for_cozonac

cozonacs_made = 0
colored_eggs = 0

while budget >= cozonac_price:
    cozonacs_made += 1
    colored_eggs += 3

    if cozonacs_made % 3 == 0:
        colored_eggs -= cozonacs_made - 2

    budget -= cozonac_price
print(f"You made {cozonacs_made} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")