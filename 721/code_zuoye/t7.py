a = input()
num = 0
str1 = 0
fu = 0
if '\n' not in a:
    for i in a:
        if i.isdigit():
            num +=1
        elif i.isalpha():
            str1 +=1

        else:
            fu +=1
else:
    for i in a:
        if i.isdigit():
            num +=1
        elif i.isalpha():
            str1 +=1
        elif i == '\\':
            break
        else:
            fu +=1



print("数字",num)
print("字符",str1)
print("符号",fu)







