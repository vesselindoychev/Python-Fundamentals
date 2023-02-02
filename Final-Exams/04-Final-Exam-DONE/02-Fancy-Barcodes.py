import re

n = int(input())

pattern = r"(@)(#)+[A-Z]{1}[A-Za-z0-9]{4,}[A-Z]{1}\1\2+"
whole_input = []
valid_barcodes = []
for i in range(n):
    barcode = input()
    whole_input = [obj.group() for obj in re.finditer(pattern, barcode)]
    valid_barcodes = []
    if whole_input:
        valid_barcodes.extend(whole_input)
        for valid_barcode in valid_barcodes:
            current_digit = ""
            for char in valid_barcode:
                if char.isdigit():
                    current_digit += char
            if current_digit == "":
                print(f"Product group: 00")
            else:
                print(f"Product group: {current_digit}")

    else:
        print(f"Invalid barcode")
