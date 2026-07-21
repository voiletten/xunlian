listi = []
for i in range(1,100):
    for j in range(1,30):
        if i+100 == j**2 :
            listi.append(i)
for i in listi:
    for j in range(1,30):
        if i + 100 + 168 == j**2:
            print(i)
