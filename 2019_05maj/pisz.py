

#           1
#    2          5
#  3    4     6 pisz('10',2,2)   7 pisz('11',2,2)


counter = 0


def pisz(s: str, n: int, k: int):
    global counter
    counter += 1

    if len(s) == n:
        print(s)
        return 0

    for i in range(1, k):
        pisz(s + str(i), n, k)


if __name__ == '__main__':

    dane = [
        ['', 3, 2],
        ["", 2, 3],
    ]

    for s, n,k in dane:
        counter = 0
        try:
            w = pisz(s, n, k)
        except:
            print('ble')

        print('count', counter)


# 111 4
#  11 3


#  1
#  2
#  4
#  8

# k ^ n + 1
