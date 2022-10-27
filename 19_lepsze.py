def foo(tab):
    n = len(tab)
    a = 0
    akt = 0
    ans = 0
    while (a < n):
        if tab[a] == a:
            akt = 0
            while a < n and tab[a] == a:
                a += 1
                akt += 1
            ans = max(ans, akt)
        elif tab[a] < a:
            akt = 0
            sum_val = tab[a]
            sum_ix = a
            a += 1
            while a < n and sum_val <= sum_ix:
                sum_val += tab[a]
                sum_ix += a
                akt += 1
                a += 1
            if sum_val == sum_ix:
                ans = max(ans, akt)
        a += 1

    return ans

t = [int(_) for _ in input().split()]

print(foo(t))
