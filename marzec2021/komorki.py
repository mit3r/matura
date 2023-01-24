


def wyr(A1, B1):

    if A1 % 2 == 1 and B1 % 2 == 1:
        return A1 + B1
    
    return A1 * B1


if __name__ == '__main__':

    dane = [
        [1, 3],
        [4, 3],
    ]

    for A1, B1 in dane:

        print(A1, B1, wyr(A1, B1))

    #P F P P

