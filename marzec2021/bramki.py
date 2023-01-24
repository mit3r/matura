


def W(a, b):

    return (not ((not a) and b)) and (not (a and (not b)))


if __name__ == '__main__':

    dane = [
        [0,0,0],
        [1,0,0],
        [0,1,1],
        [1,1,1],
    ]

    for a, b, w in dane:

        print('P' if W(a, b) == w else 'F')

    