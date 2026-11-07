import time
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

bfib = fib()

while True:
    print(next(bfib), end=" ", flush=True)
    time.sleep(0.5)
