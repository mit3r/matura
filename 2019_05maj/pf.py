



# 3.1 F P P F


def quad(n):

    n = bin(n)[2:]

    even = n[::2]
    odd = n[1::2]

    return "".join(map( str,[int(e+o, 2) for e, o in zip(even, odd)]))


w = 0b1111110 * 0b101

print(quad(w))
print(bin(w))
print(oct(w))
print(hex(w))

# 3.2 P F P P

# 3.3 P P F F 