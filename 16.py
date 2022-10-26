def foo(t):
    t.sort()
    return t[0] != t[1] and t[-1] != t[-2]

n = int(input())

t = [0 for i in range(n)]

for i in range(n):
    t[i] = int(input())

print(foo(t))
