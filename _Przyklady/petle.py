import random


def daj_sito(n):

    sito = [True for i in range(0, n+1)]

    sito[0] = False
    sito[1] = False

    for i in range(2, n+1):

        if sito[i]:
            j = i*2

            while j <= n:
                sito[j] = False
                j += i

    return sito




if __name__ == '__main__':
    pierwsze = daj_sito(20)

    print(2, pierwsze[2])
    print(13, pierwsze[13])
    print(8, pierwsze[8])










