def nwd(a, b):
    if b == 0:
        return a
    return nwd(b, a%b)

def foo(t):
    ctr = 0
    for i in range(0, len(t-2):
        if nwd(nwd(t[i], t[i+1]), t[i+2]) == 1:
            ctr += 1
        if i+3 < len(t) and nwd(nwd(t[i], t[i+1], t[i+3])):
            ctr += 1
        if i+3 < len(t) and nwd(nwd(t[i], t[i+2]), t[i+3]):
            ctr += 1
        if i+3 < len(t) and nwd(nwd(t[i+1], t[i+2], t[i+3])):
            ctr += 1

    return ctr

            