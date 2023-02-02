username = input().split(', ')
res = []
for name in username:
    if 3 < len(name) < 16 and name.isalnum() or '-' in name or '_' in name:
        res.append(name)

print('\n'.join(res))