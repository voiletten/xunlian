a = input()
# m t w t f s s
if a[0]=="w":
    print("周3")
if a[0]=="m":
    print("周一")
if a[0]=="f":
    print("周五")

if a[0]=="t":
    if a[1]=="h":
        print("周四")
    else:
        print("周二")
if a[0]=="s":
    if a[1]=="a":
        print("周六")
    else:
        print("周日")

