def foo(n):
    tab = [True for i in range(n+1)]
    tab[0] = tab[1] = False

    i = 2
    while i*i < n:
        if tab[i]:
            for j in range(i*i, n+1, i):
                tab[j] = False
        i += 1


    for i in range(n+1):
        if tab[i]:
            print(i)

    
foo(int(input()))
