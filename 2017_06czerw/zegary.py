

def quad(n):

    n = bin(n)[2:]

    if len(n) % 2 == 1:
        n = '0' + n

    even = n[::2]
    odd = n[1::2]

    return [int(e+o, 2) for e, o in zip(even, odd)]


print('A', int('00010110100', 2))
print('B', int('000330', 4))
print('C', int('078', 16))

wyniki = [180, 60, 120]

print([w for w in wyniki if w % 9 == 0])
print([w for w in wyniki if w % 6 == 0])


# F P P F

for x1 in range(0, 1 + 1):
    for x2 in range(0, 1 + 1):
        a = int('000110100' + str(x1) + str(x2), 2)
        print('Dla', x1, x2)
        b = a - 120
        c = a - 60

        print('B', quad(b))
        print('C', hex(c))

# 000110100_10
# 001_12_2
# 0_96
