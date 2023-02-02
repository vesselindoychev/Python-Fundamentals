old_version = input().split(".")

old_version = int("".join(old_version))
new_version = str(old_version + 1)
print(".".join(new_version))


# old_version = list(map(int, input().split(".")))
#
# old_version[-1] += 1
# if old_version[-1] >= 10:
#     old_version[-1] = 0
#     old_version[-2] += 1
#
# if old_version[-2] >= 10:
#     old_version[-2] = 0
#     old_version[-3] += 1
# print(".".join(list(map(str, old_version))))
