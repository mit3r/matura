

liczba = int('BA', 16)

print(liczba)
print(oct(8))
print(bin(liczba))


def quadratic(n):

    n = bin(n)[2:]

    if len(n) % 2:
        n = '0' + n

    even = n[::2]
    odd = n[1::2]

    w = [int(e+o, 2) for e, o in zip(even,odd)]

    return w

# P F P F

print(liczba, quadratic(liczba))