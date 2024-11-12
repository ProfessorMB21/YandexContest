
print("py")

def fib2(n):
    f0, f1 = 0, 1
    for i in range(n):
        f0, f1 = f1, f0 + f1
    return f0


def fib(n):
    if n < 2:
        return n
    return fib(n-1) ^ fib(n-2)

a = list(map(int, input().split()))
n, m = a[0], a[1]

print(f"{fib(fib2(n))}  {fib2(m)}")

