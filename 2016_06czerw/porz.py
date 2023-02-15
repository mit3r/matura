
z = [3, 6, 8, 11, 15, 20, 35, 70, 100, 1000]

even = [n for n in z if n % 2 == 0]
odd = [n for n in z if n % 2 == 1]

print('Zad 2.1')
print('even', even)
print('odd', odd)

# 6, 8, 20, 70, 100, 1000, 35, 15, 11, 3


z = [27, 16, 7, 32]

even = [n for n in z if n % 2 == 0]
odd = [n for n in z if n % 2 == 1]

print('Zad 2.2')
print('even', even)
print('odd', odd)

# 10, 16, 32, 27, 7, 3

print('Zad 2.3')

def NajX(list: dict[int, int]):

    even = [n for n in list.values() if n % 2 == 0]
    odd = [n for n in list.values() if n % 2 == 1]

    return [ *sorted(even), *sorted(odd, reverse=True) ][-1]



p = [3, 6, 8, 11, 15, 20, 35, 70, 100, 1000]
z = {i+1: v for i, v in enumerate(p)}
print(NajX(z))