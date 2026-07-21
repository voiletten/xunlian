# def sum(a):
#     if a == 1:
#         return 1
#     return sum(a * 1/2 -1)



def sum(a,count):

    if count == 0:
        return a
    count -= 1
    return sum((a+1) * 2,count)

print(sum(1,10))
