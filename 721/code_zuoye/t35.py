list1 = []
min = 9999999
max = 0
index_min = -1
index_max = -1
for i in range(3):
    a = int(input())
    if a > max:
        max = a
        if i != 0:
            index_max = len(list1)
    if a < min:
        min = a
        if i != 0:
            index_min = len(list1)
    list1.append(a)
list1[index_min],list1[len(list1)-1] = list1[len(list1)-1],list1[index_min]
list1[index_max],list1[0] = list1[0],list1[index_max]
print(list1)

