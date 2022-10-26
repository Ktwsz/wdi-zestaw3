def foo(t):
    sum_val, sum_ix, ans, temp_ans = 0, 0, 0, 0

    for i in range(len(t)):
        sum_val += t[i]
        sum_ix += i
        
        if sum_ix != sum_val or t[i] <= t[max(i-1, 0)]:
            sum_val = t[i]
            sum_ix = i
            ans = max(ans, temp_ans)
            temp_ans = 1 
        elif sum_val == sum_ix:
            temp_ans += 1
        
    ans = max(ans, temp_ans)
    return ans

t = [int(_) for _ in input().split()]

print(foo(t))
