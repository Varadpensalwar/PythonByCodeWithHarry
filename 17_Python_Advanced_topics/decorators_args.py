def reapet(n):
    def decorator(func):
        def wrapper(a):
            for _ in range(n):
                func(a)
        return wrapper
    return decorator

@reapet(7)
def say_hello(a):
    print(f"Hello! {a}")

say_hello("Varad")