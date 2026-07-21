import math


def func(a):
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True




n = int(input())
if n % 2 == 0:
    for i in range (1, n // 2 + 1):
       if func(i) and func(n-i):
           print(n,i,n-i)


else:
    print("??")