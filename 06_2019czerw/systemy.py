

def quad(n):

    n = bin(n)[2:]

    if len(n) % 2:
        n = '0' + n

    even = n[::2]
    odd = n[1::2]

    return "".join(map(str, [int(e+o, 2) for e, o in zip(even, odd)]))


w = int('11001001', 2) - int('1111111', 2)

print(hex(w))
print(oct(w))
print(quad(w))
print(bin(w))

# F P F P




