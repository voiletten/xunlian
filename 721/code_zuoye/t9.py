sum = 1
for i in range(6,1000):
    sum = 1
    for j in range(1,i):
        if i%j==0:
            sum *= j
            if sum == i :
                print(i)
                break

