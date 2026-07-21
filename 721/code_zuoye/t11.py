i = 0
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            if a != b and a != c and b != c:
                print(a*100+b*10+c)
                i+=1
print("一共",i)