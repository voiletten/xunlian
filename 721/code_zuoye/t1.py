#  1.

def rabbit(n):
    if n == 1 or n == 2:
        return 1
    return rabbit(n-1)+rabbit(n-2)

rabbit = rabbit(10)
print(rabbit)
