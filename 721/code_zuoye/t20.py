
s = 0
def sum(a,b,count):
    global s
    s += (a/b)
    t = b
    b = a
    a = t + a
    count = count - 1
    if count == 0:
        return s
    return sum(a,b,count)
result = sum(2,1,20)
print(result)


