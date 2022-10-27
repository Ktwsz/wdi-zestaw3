def foo(n):
    a = 10**n
    sum = 0
    i = 2
    k = 2
    while a//k != 0:
        sum += a//k
        i += 1
        k *= i

    return sum

print(foo(int(input())))
