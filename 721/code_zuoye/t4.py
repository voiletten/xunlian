#4
n = int(input("输入数字"))
k = 2
while k <= n:
    if n == k:
        print("已经结束")
        print(k)
        break
    if n != k:
        if n % k == 0:
            n //= k
            print(k)
            k =2
        else:
            k += 1




