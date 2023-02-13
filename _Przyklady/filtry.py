
from random import *


# w = [ True for i in range(10)]


# print(w)

# liczby = [1, 32, 64, 82, 91, 2137, 11, 121, 82, 94349, 9, 8]

# pal = [n for n in liczby if n == int(str(n)[::-1])]

# print(pal, len(pal))


liczby = [ list(map( int, line.strip().split(' '))) for line in open('./_Przyklady/filtry.txt', 'r')]

dane = [
    ('di', 2),
    ('ze', 3),
    ('ja', 0),
]

print(max(dane, key=lambda x: x[1]))

