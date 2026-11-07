from functools import wraps

def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper

@count_calls
def say_hello():
    print("Привет!")

@count_calls
def add(a, b):
    return a + b

say_hello()
say_hello()
add(2, 3)

print(f"say_hello вызвана: {say_hello.calls} раз(а)")
print(f"add вызвана: {add.calls} раз(а)")