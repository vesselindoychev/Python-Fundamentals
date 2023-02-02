# import re
# text = input()
#
# pattern = r"\+359( |-)2\1\d{3}\1\d{4}\b"
#
# valid_numbers = [obj.group() for obj in re.finditer(pattern, text)]
# print(', '.join(valid_numbers))



# import re
#
# text = input()
# valid_numbers = []
#
# pattern = r"\+359 2 \d{3} \d{4}|\+359-2-\d{3}-\d{4}\b"
#
#
# match = re.findall(pattern, text)
# print(', '.join(match))


import re

text = input()
pattern = r"\+359(?P<separator>( |-))2(?P=separator)\d{3}(?P=separator)\d{4}\b"

valid_numbers = [obj.group() for obj in re.finditer(pattern, text)]
print(', '.join(valid_numbers))