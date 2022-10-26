tab = []

a = int(input())
tab.append(a)

while a != 0:
    a = int(input())
    tab.append(a)

tab.sort()
print(tab[10])
