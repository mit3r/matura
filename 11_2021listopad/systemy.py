



suma = int('223101', 4) + int('3741', 8) + int('F0A', 16)

print(bin(suma))

b = bin(suma)[2:]
quad = [str(int(b[i:i+2], 4)) for i in range(0, len(b), 2)]
quad = "".join(quad)
print(quad, '4')
print(oct(suma))
print(hex(suma))

#P F F P


d = [3.5 * 2, 2.2 * 3, 4.5 *3, 2.4, 2.1 * 2 ]

print(sum(d))