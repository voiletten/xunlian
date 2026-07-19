
#无参 class :  __init__(func)  __call__(*args,**kwargs)

class LogDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"=====开始执行函数{self.func.__name__}==========")
        result = self.func(*args, **kwargs)
        print(f"=====函数执行结果：{result}==========")
        return result
@LogDecorator
def mul(a, b):
    return a - b
print(mul(2,3))


#有参 __init__ (装饰器参数)  __call__(func,wrapper(*args,**kwargs))

class Logger:
    def __init__(self,level="INFO"):
        self.level = level

    def __call__(self, func):
        def wrapper(*args,**kwargs):
            print(f"[{self.level}]调用函数:{func.__name__}")
            return func(*args,**kwargs)
        return wrapper

@Logger("DEBUG")
def login(name):
    print(f"登录用户{name}")

login("张三")








