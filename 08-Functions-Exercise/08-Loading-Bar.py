def loading_bar(number):
    percent_sign = (number // 10) * "%"
    dots = ((100 - number) // 10) * "."
    if number == 100:
        return f"{number}% Complete!\n[{percent_sign}]"
    else:
        return f"{number}% [{percent_sign + dots}]\nStill loading..."


number = int(input())
print(loading_bar(number))