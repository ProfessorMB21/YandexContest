
def lastDigit(n):
    return n % 10

def fib(n):
    f0, f1 = 0, 1
    for i in range(n):
        f0, f1 = f1, f0 + f1
    return f0

n = int(input())
m = int(input())

print(fib(n) % fib(m))