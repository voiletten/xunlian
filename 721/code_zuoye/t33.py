rows = 10
triangle = []

for i in range(rows):
    row = [1] * (i + 1)          # 每行首尾都是1
    for j in range(1, i):
        row[j] = triangle[i-1][j-1] + triangle[i-1][j]
    triangle.append(row)

# 居中打印
max_width = len(" ".join(map(str, triangle[-1])))
for row in triangle:
    print(" ".join(map(str, row)).center(max_width))