def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
    return True

def gen():
    t = [0, 1]
    while t[-1] <= 1000000:
        t.append(t[-1]+t[-2])
    return t

def foo(fib, t):
    fib_ix = 0
    flag = True
    for i in range(len(t)):
        if i == fib[fib_ix]:
            if not is_prime(t[i]):
                return False
            fib_ix += 1
        elif flag:
            flag = is_prime(t[i])

    return flag
        
n = int(input())

t = [0 for i in range(n)]

for i in range(n):
    t[i] = int(input())

print(foo(gen(), t))

    