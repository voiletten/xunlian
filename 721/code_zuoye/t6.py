#6

def cal(a,b):
    if b > a:
        a,b = b,a
    while True:
        t = b
        b = a % b
        a = t
        if b == 0:
            print(a)
            break
    return a

print(30 * 50 // cal(30,50))


