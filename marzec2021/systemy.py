

def quadratic(n):

    n = bin(n)[2:]

    if len(n) % 2:
        n = '0' + n

    even = list(n[::2])
    odd = list(n[1::2])

    return [int(e+o, 2) for e, o in zip(even, odd)]

def odp(cond):
    print('P' if cond else 'F')

if __name__ == '__main__':

    n = int('1011101', 2) - int('10111', 2)

    dane = [
        n < int('100111', 2),
        n == int('1000110', 2),
        n > int('10111', 2),
        n == int('1001000', 2),
    ]

    for w in dane:
        odp(w)