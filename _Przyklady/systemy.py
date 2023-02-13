def quad(n):

    n = bin(n)[2:]

    if len(n) % 2 == 1:
        n = '0' + n

    even = n[::2]
    odd = n[1::2]   

    return [int(e+o, 2) for e, o in zip(even, odd)]



w = int('3211', 4) + int('2322', 4)


print(quad(w))
print(hex(w))





quad(12)