def zamiera(ciag, n):

    for i in ciag:
        if i == n:
            return True

    return False


def ilepodmian(ciag: list):

    n = len(ciag)

    podmian = 0
    for i in range(n):

        if not zamiera(ciag, i+1):
            podmian += 1

    return podmian
        
            


if __name__ == '__main__':

    ciagi = [
        [1, 3, 1],
        [1, 4, 2, 5],
        [2,2,2,2,2],
        [4,2,3,1],
        [5,4,1,5,6,8],
        [8,4,9,6,5,7],
    ]

    for ciag in ciagi:
        print(ilepodmian(ciag))