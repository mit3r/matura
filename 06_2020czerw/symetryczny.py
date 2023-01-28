
ilosc = 0


def sym(a, b):
    global ilosc
    if a != 0:
        sym(a - 1, b + 1)
        # print(a * b, end=' ')
        ilosc += 1
        sym(a- 1 , b + 1)

dane = [
    [3,2],
    [4,4],
    [5,1],
    [6,6],
    [10, 2020],
]

for a, b in dane:
    ilosc = 0
    sym(a, b)
    print(ilosc)