

def quad(n):

    n = bin(n)[2:]
    if len(n) % 2:
        n = '0' + n

    even = n[::2]
    odd = n[1::2]

    return ''.join(map(str,[int(e+o, 2) for e, o in zip(even,odd)]))


r = int('11001001', 2) - int('1111110', 2)
r = int('1'+'0'*15, 2)

print('r:', r)

print(quad(r))
print(oct(r))
print(hex(r))
print(r)

# F P P F

# F P F F

# F F P P
