


w = int('101101', 2) + int('111011', 2)

print(bin(w))

print(hex(w))

print(oct(w))

b = bin(w)[2:]
b = '0' + b
print(b[2:])


quad = [b[c : c+2] for c in range(0, len(b), 2)]

print(quad)

# 1 2 2 0

