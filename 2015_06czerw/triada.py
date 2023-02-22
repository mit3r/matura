

dane = [2, 3, 5, 6, 9, 10, 11, 13, 14, 15, 17, 19, 20, 23, 24]
a = 5
b = 15
print(len([c for c in dane if all([c < a + b, a < c + b, b < a + c])]))




def triady(lista: list[int]):

    c1, c2 = lista[:2]

    ok = 0
    for k in lista:
        if c1 + c2 > k and c1 + k > c2 and c2 + k > c1:
            ok += 1

    return ok


print(triady([5, 15, 2, 3, 5, 6, 9, 10, 11, 13, 14, 15, 17, 19, 20, 23, 24]))