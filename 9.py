def foo(t):
    last, mx = -1, 0
    temp_mx = 0

    for i in t:
        if last < i:
            temp_mx += 1
        else:
            mx = max(temp_mx, mx)
            mx_temp = 0

        last = i

    mx = max(temp_mx, mx)
    return mx

n = int(input())
t = [0 for i in range(n)]
for i in range(n):
    t[i] = int(input())


print(foo(t))
