def func(a):
    if a==1:
        return 1
    return func(a-1)*a
print(func(5))