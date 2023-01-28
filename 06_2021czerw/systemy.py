


a = int('10101', 2) + int('101011', 2)
b = int('111111', 2)

print( a == b )

a = int('a', 16) + int('b', 16)
b = int('f', 16)

print( a == b )

a = int('12', 8) * 2
b = int('14', 16)

print( a == b )

a = 123
b = int('1111101', 2)

print( a == b)


w = 12
b = bin(12)[2:]

quad = [ int( b[i:i+2], 2) for i, v in enumerate(b) if not i % 2]


print(quad)