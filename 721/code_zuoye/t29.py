list1 = []
sum = 0
for i in range(3):
    row = []
    for j in range(3):
        row.append(int(input()))
    list1.append(row)
for i in range(3):
    for j in range(3):
        if i == j:
            sum += list1[i][j]
        if (i + j) == 3:
            sum += list1[i][j]

print(sum)
