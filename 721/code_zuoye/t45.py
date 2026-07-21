import math


def func(a):
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True


n = int(input())
if func(n):
    count = 0
    while n >9:
        n-=9
        count += 1
    print(count)
else:
    print("False")