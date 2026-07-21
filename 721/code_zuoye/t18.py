list1 =["a","b","c"]
list2 = ["x","y","z"]

for i in list1:
    for j in list2:
        if (i == "c" and (j == "x" or j=="z")) or (i == "a" and j == "x"):
            continue

        print(f"{i} vs {j}")