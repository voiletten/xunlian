for i in range(100,1000):
    b = i // 100
    g = i % 10
    s = (i % 100) // 10
    if g**3 + b**3 + s**3 == i:
        print(i)