

def wyznacz_b(M, a, x):
    pot = 1
    if x != 0:
        pot = a

        for p in range(x-1):
            pot *= a

    return pot % M

def wyznacz_x(M, a, b):

    x = 0
    while b != wyznacz_b(M, a, x):
        x += 1

    return x

if __name__ == '__main__':

    print(wyznacz_b(7, 2, 5))
    print( 'b', wyznacz_b(11, 3, 3))
    print('x', wyznacz_x(31, 5, 25))
    print('x', wyznacz_x(59,2,5))
    print('b', wyznacz_b(80, 9, 2))

    