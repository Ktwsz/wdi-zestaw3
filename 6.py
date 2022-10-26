import random as r

def check(a):
    while a > 0:
        if a % 10 % 2 == 1:
            return True
        a //= 10
    return False

n = int(input())

tab = [r.randrange(1, 1000) for i in range(n)]

for i in tab:
    if check(i):
        print(i)
