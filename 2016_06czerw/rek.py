import numpy as np

def silnia(n):
    w = 1
    for i in range(2, n+1):
        w *= i

    return w


def F(n):

    if n in [1, 2]:
        s = n
    else:
        s = n*F(n-2)

    return s * (n+1)


def F_wyw(n):
    print(f'F({n})')

    if n in [1, 2]:
        s = n
    else:
        s = n * F_wyw(n-2)

    return s * (n+1)


print('Zad 1.1')
for n in [1, 2, 3, 4, 5, 6]:
    print('n:', n, 'F(n)', F(n))

    print('a', (n+1)*(n+2)/2)
    print('b', silnia(n+1))
    print('c', n ** (n // 2))


print('Zad 1.2')

F_wyw(11)


print('Zad 1.3')
#B