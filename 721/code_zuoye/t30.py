list1 = [1,3,5,7,9,11]
a = int(input())
b = 0
for i in list1:
    if i > a:

        b = list1.index(i)
        print(b)
        break
list2 = list1[:b] + [a] + list1[b:]
print(list2)



