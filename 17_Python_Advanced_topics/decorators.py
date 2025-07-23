def Decorator(func):
    def wrapper():
        print("going to execute")
        func()
        print("executed")
    return wrapper

def hello_finc():
    print("Hello!")


f=  Decorator(hello_finc)
f()