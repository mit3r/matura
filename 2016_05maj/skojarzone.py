import math


def dzielniki(n: int):
    return [i for i in range(1, n) if n % i == 0]

def skojarzone(a: int, b: int):

    da = dzielniki(a)
    db = dzielniki(b)
    print(f'dla {a}, {b}')
    print(a, da, sum(da))
    print(b, db, sum(db))

    return sum(da) == b+1 and sum(db) == a+1
        
# dane = [
#     [78, 64],
#     [20,21],
#     [75,48],
# ]

# for a, b in dane:
#     print(skojarzone(a, b))

def znajdz_skojarzenie(a: int):

    suma_a = 0

    for i in range(1, int(math.sqrt(a))+1):
        if a % i == 0:
            suma_a += (i + a // i)
    suma_a -= a


    b = suma_a - 1
    suma_b = 0

    for i in range(1, int(math.sqrt(b))+1):
        if b % i == 0:
            suma_b += (i + b // i)
    suma_b -= b

    return b if suma_b == a + 1 else False

print(znajdz_skojarzenie(75))




