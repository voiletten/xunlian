def func(a):
    if a==1:
        return 1
    return func(a-1)*a
sum = 0
for i in range(1,21):
    sum += func(i)
print(sum)