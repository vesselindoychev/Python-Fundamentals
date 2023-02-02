text = input()

res = []
res2 = 0
extensions = {}
tokens = text.split('\\')

res.append(tokens[-1])
res = '.'.join(res)
res2 = res.split('.')

extensions[res2[0]] = res2[1]
# print(f"File name: {res2[0]}")
# print(f"File extension: {res2[1]}")

for key, value in extensions.items():
    print(f"File name: {key}")
    print(f"File extension: {value}")