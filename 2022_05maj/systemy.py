



w = int('132', 4) + int('3111', 4)

print(bin(w))

print(oct(w))

print(hex(w))

b = bin(w)[2: ]
print(b)

quad = [int(b[i : i+2], 2) for i in range(0, len(b), 2)]

print(quad)