def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1

    return True

def check(n):
    ans = []
    i = 1
    while i*i < n:
        if n % i == 0:
            if is_prime(i): ans.append(i)
            if is_prime(n//i): ans.append(n//i)

        i += 1
    return ans

def bfs(t):
    last = len(t)-1

    queue = [0]
    while len(queue) != 0:
        top = queue[0]
        print(top)
        queue.pop(0)

        for i in check(t[top]):
            if top+i == last:
                return True
            elif top+i < last:
                queue.append(top+i)
            
    return False


n = int(input())
t = [0 for i in range(n)]
for i in range(n):
    t[i] = int(input())

print(bfs(t))

