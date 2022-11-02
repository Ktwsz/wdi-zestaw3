from random import randrange
def foo(t):
    asc_len, asc_len_temp = 1, 1
    des_len, des_len_temp = 1, 1
    r = t[1]-t[0]
    for i in range(1, len(t)):
        if t[i]-t[i-1] == r:
            if r > 0:
                asc_len += 1
            elif r < 0:
                des_len += 1
        else:
            if r > 0:
                asc_len = max(asc_len, asc_len_temp)
            elif r < 0:
                des_len = max(des_len, des_len_temp)

            asc_len_temp = 2
            des_len_temp = 2
            r = t[i]-t[i-1]

    if r > 0:
        asc_len = max(asc_len, asc_len_temp)
        asc_len_temp = 2
    elif r < 0:
        des_len = max(des_len, des_len_temp)
        des_len_temp = 2

    return asc_len-des_len

n = int(input())
t = [randrange(1, 99, 2) for i in range(n)]

print(t)

print(foo(t))
