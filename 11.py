def foo(t):
    if len(t) == 1:
        return -1
    q = t[1]/t[0]
    mx_temp, mx = 2, 2
    for i in range(2, len(t)):
        if t[i]/t[i-1] == q:
            mx_temp += 1
        else:
            mx = max(mx, mx_temp)
            mx_temp = 2
            q = t[i]/t[i-1]
    
    mx = max(mx, mx_temp)
    return mx


n = int(input())
t = [0 for i in range(n)]
for i in range(n):
    t[i] = int(input())

print(foo(t))
