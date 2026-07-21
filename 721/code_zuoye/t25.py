# a = input('shuru')
# list1 = []
# for i in a:
#     list1.append(i)
# list2 = list1[::-1]
#
# if list1 == list2:
#     print("回文",a)
a = input('输入字符串：')

if a == a[::-1]:
    print("回文", a)
else:
    print("不是回文")