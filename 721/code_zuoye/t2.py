import math
list1 = []
for i in range(101,201):
    for j in range(2,int(math.sqrt(i))):
        if i%j == 0:
            break
        else:
            list1.append(i)
            break

print(list1)