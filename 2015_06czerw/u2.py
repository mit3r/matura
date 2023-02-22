

# print(93, bin(93)[2:])
# # 01011101

# # -128 + x = -42
# # 128 - x = 42
# x = 128 - 42

# print(bin(x)[2:])
# # 11010110

# w = int('00101011',2) + int('011011',2) -  128

# print(f'1{bin(128 - 58)[2:]}')
# # 11000110



def neg(b):
    if b not in ['0', '1', 0, 1]:
        raise ValueError('This is not a valid argument, not [0, 1]')

    if type(b) == int:
        return 0 if b == 1 else 1

    return '0' if b == '1' else '1'

def przeciwna(a: list[int], n: int):

    b = [0 for _ in range(n)]

    i = 0
    while a[i] == 0:
        b[i] = 0
        i += 1
    
    b[i] = a[i]
    while i < n:
        b[i] = neg(a[i])
        i += 1
    
    return b

w = [ str(i) for i in przeciwna([int(b) for b in '1111001001110000'], 16)]
w.reverse()
print(''.join(w))
# 0000110110001111
# 1111111111111111
# 0000000001111111

