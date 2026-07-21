from itertools import permutations

list1 = [0, 1, 2, 3, 4, 5, 6, 7]
count = 0

for length in range(1, 9):                 # 位数
    for num in permutations(list1, length):
        if num[0] == 0:                    # 不能以 0 开头
            continue
        if num[-1] in [1, 3, 5, 7]:        # 奇数
            count += 1

print(count)