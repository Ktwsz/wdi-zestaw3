from random import randrange
def foo(t):
    day = [0 for i in range(7)]

    for i in t:
        if day[i] == 1:
            return True
        else:
            day[i] = 1

    return False



for n in range(20, 41):
    ctr = 0
    for j in range(10000):
        t = [randrange(0, 7) for x in range(n)]
        if foo(t):
            ctr += 1
        
    print(n, ctr/10000)

