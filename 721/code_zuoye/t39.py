
def func(a):
    if a % 2 == 0:
        if a == 2:
            return 0.5
        return func(a-2) + 1/a
    else:
        if a == 1:
            return 1
        return func(a-2) + 1/a
print(func(5))
print(func(8))