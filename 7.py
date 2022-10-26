import random as r

def check(a):
    while a > 0:
        if a % 10 % 2 == 0:
            return False
        a //= 10
    return True

n = int(input())

tab = [r.randrange(1, 1000) for i in range(n)]

for i in tab:
    if check(i):
        print(i)
