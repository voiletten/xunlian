

count = 5
def func(x,count):
    if count == 0:
        return x
    count -= 1
    if x % 4 != 0:
        return None
    return func(1+ x * 5//4,count)
for i in range(9999):
    if i % 4==0:
        a = func(i, 5)
        if a != None:
            print(a)


