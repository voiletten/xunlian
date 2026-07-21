n = int(input())
list1 = [i for i in range(1,n+1)]
count = 1
index = 0

while len(list1) > 1:
    if count == 3:
        list1.pop(index)
        count = 1
    else:
        count += 1
        index += 1
    if index == len(list1):
        index = 0


print(*list1)