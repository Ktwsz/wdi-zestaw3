import random as r

def check(t, t_temp):
    ix = 0
    for i in range(len(t)):
        if ix == len(t_temp):
            return True
        if t[i] == t_temp[ix]:
            ix += 1
        else:
            ix = 0
    return ix == len(t_temp)

def foo(t):
    ix = 0
    ans = 0

    for i in range(len(t)+1):
        for j in range(i+1, len(t)+1):
            t_temp = t[i:j]
            t_temp.reverse()

            if check(t, t_temp):
                ans = max(ans, j-i)

    return ans

n = int(input())

t = [r.randrange(100, 1000) for i in range(n)]

print(foo(t))
