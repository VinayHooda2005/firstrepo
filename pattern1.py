n=7

for i in range(1, n+1):
    if i == 1 or i == n:
        print('*' * n)
    else:
        print(' ' * (n - 4) + '*')
print(end=' ')
print()

for r in range(6):
    for c in range(7):
        if ((r == 0 and c % 3 != 0) or (r == 1 and c % 3 == 0)
                or (r - c == 2) or (r + c == 8)):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
print(end=' ')
print()

for i in range(1, n + 1):
    if i == n:
        print('*' * i)
    else:
        print('*' + ' ' * (n - 2) + '*')
print(end='')
print()
