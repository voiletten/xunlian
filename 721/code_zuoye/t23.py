def func(a,count):
    if count==1:
        return a
    count -=1
    print("年纪",a+2)
    return func(a+2,count)
result = func(10,5)
