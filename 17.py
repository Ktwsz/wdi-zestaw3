def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i += 1

    return True


def sum(a, b, mask_a, mask_b):
    ans = 0

    for i in range(len(a)):
        if mask_a%2 == 1:
            ans += a[i]
        mask_a //= 2

    for i in range(len(b)):
        if mask_b%2 == 1:
            ans += b[i]
        mask_b //= 2

    return ans

def foo(a, b):
    ans = 0
    for i in range(1, 2**len(a)):
        for j in range(1, 2**len(b)):
            if is_prime(sum(a, b, i, j)):
                ans += 1

    return ans

a = [int(_) for _ in input().split()]
b = [int(_) for _ in input().split()]

print(foo(a, b))
