x = int(input())
y = int(input())
z = int(input())


print(((x if x < z else z) if x < y else (y if y < z else z)))


