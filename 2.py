def foo(a, b):
    check_a = [0 for i in range(10)]
    check_b = check_a[:]

    while a > 0:
        check_a[a%10] += 1
        a //= 10
    while b > 0:
        check_b[b%10] += 1
        b //= 10

    for i in range(10):
        if check_a[i] != check_b[i]:
            return False
    return True


a = int(input())
b = int(input())

print(foo(a, b))
    