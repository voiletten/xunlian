from unittest import result

a = input('a')
b = int(input('b'))

sum = 0
s = 0
for i in range(1,b+1):
    s += int(a * i)
    sum += s
print(sum)