year = int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入日期："))

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]#ping
sum = 0

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    months[1] += 1
    for i in range(month-1):
        sum += months[i]
else:
    for i in range(month-1):
        sum += months[i]
print(sum+day)