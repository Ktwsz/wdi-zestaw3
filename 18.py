def check(t):
    i = 0
    rev_i = len(t)-1

    while i < rev_i:
        if t[i] != t[rev_i] and (t[i]%2 == 0 or t[rev_i]%2 == 0):
            return False
        else:
            i += 1
            rev_i -= 1

    return True


def foo(t):
    ix = 0
    ans, temp_ans = t[0]%2, t[0]%2

    for i in range(1, len(t)):
        if check(t[ix:i+1]):
            temp_ans += 1
        else:
            ans = max(ans, temp_ans)
            temp_ans = t[i]%2
            ix = i

    ans = max(ans, temp_ans)
    return ans


t = [int(_) for _ in input().split()]

print(foo(t))