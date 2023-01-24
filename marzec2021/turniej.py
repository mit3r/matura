# n = 2 4 8 16 32 64 ... etc

# i-ty mecz grają 2*(i-1) i 2*(i-1) + 1

def kiedy_graja(x, y):

    print(f'dla {x}, {y}: ')

    runda = 0
    while x != y:
        runda += 1

        x //= 2
        y //= 2

        print(f'x={x}, y={y}')

    return runda



if __name__ == '__main__':

    dane = [
        [2,6],
        [0,3],
        [3,7],
        [16,30],
        [0, 7]
    ]

    for x, y in dane:
        print(x, y, 'runda', kiedy_graja(x,y))
