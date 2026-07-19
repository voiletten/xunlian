def a(func):
    def wrapper(*args, **kwargs):
        print("装饰器")
        a = func(*args, **kwargs)
        return a
    return wrapper

@a
def b(i):
    return i
print(b(2))