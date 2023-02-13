


def sito(n):

    sito = [True for i in range(n + 1)]

    sito[0] = False
    sito[1] = False

    for i in range(2, n+1):

        if sito[i]:
            j = i * 2

            while j <= n:
                sito[j] = False
                j += i
    
    return sito


def z(nr):
    print( f'Zad 4.{nr}' )

if __name__ == '__main__':

    pierw = sito(10_001)

    pary = [line.strip().split() for line in open('punkty.txt', 'r')]

    z(1)

    odp = len([ 1 for x, y in pary if pierw[int(x)] and pierw[int(y)]])

    print(odp)

    z(2)

    odp = len([1 for x, y in pary if set(x) == set(y) ])
    print(odp)

    z(3)

    pary = [(int(x), int(y)) for x, y in pary]

    maks_distance = 0
    a = []
    b = []

    for xa, ya in pary:
        for xb, yb in pary:

            distance = ( (xb - xa) ** 2 + (yb - ya) ** 2 )**(1/2)

            if distance > maks_distance:
                a = xa, ya
                b = xb, yb
                maks_distance = distance

    print('A', a)
    print('B', b)
    print('Dist', round(maks_distance))

    z(4)

    bok = 10_000 // 2
    print('wewnątrz', len([1 for x, y in pary if x < bok and y < bok]))
    print('na bokach', len([1 for x, y in pary if (x == bok and y <= bok) or (y == bok and x <= bok)]))
    print('na zewnatrz', len([1 for x, y in pary if x > bok or y > bok]))