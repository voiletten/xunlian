
list2 = []
def lock(a):
    list1 = list(a)
    for i in list1:
        list2.append( (int(i)+5)%10)
    list2[0],list2[3] = list2[3],list2[0]
    list2[1],list2[2] = list2[2],list2[1]
    print(*list2)

lock("5580")

