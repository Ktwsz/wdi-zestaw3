def check(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n%i == 0:
            n //= i
            if n % i == 0:
                return False

        i += 1
            
    return True

def foo(t):
    il = 1
    ans = 0
    temp_ans = 0
    for i in t:
        il *= i
        if check(il):
            temp_ans += 1
        else:
            il = i
            ans = max(ans, temp_ans)
            temp_ans = 1

    ans = max(ans, temp_ans)
    
    return ans

t = [int(_) for _ in input().split()]

print(foo(t))
