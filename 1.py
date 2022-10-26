import math as m

def foo(a, n):
    print(int(m.log(a, n))+1)
    ans = [0 for i in range(int(m.log(a, n))+1)]

    i = len(ans)-1
    while a > 0:
        ans[i] = a%n
        a //= n
        i -= 1

    for i in ans:
        if i > 9:
            print(chr(ord('A')+i-10), end="")
        else:
            print(i, end="")

a = int(input())
n = int(input())

foo(a, n)
