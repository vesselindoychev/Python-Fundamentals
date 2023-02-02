first_value = int(input())
second_value = int(input())

print(f"Before:\na = {first_value}\nb = {second_value}")

first_value, second_value = second_value, first_value

print(f"After:\na = {first_value}\nb = {second_value}")