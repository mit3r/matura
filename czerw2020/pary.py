

def sitoera(n):
    sito = [True for i in range(n)]

    sito[0] = False
    sito[1] = False

    i = 2
    while i < n:
        if i:
            j = i
            while j + i < n:
                j += i
                sito[j] = False
        i += 1

    sito[2] = False
    return sito


if __name__ == '__main__':

    pary = [line.strip().split() for line in open('pary.txt', 'r')]
    pary = [[int(liczba), napis] for liczba, napis in pary]

    liczby = [liczba for liczba, napis in pary]

    sito = sitoera(101)

    print('Zad 4.1')
    for liczba in liczby:
        for i in range(3, liczba):
            if sito[i] and sito[liczba-i]:
                print(liczba, i, liczba - i)
                break

    print('Zad 4.2')

    napisy = [napis for liczba, napis in pary]

    for napis in napisy:

        big_c = ' '
        big_l = 0

        temp_c = ' '
        temp_l = 0

        for pivot, char in enumerate(napis):
            temp_l += 1

            if char != temp_c:
                temp_l = 1
                temp_c = char

            if temp_l > big_l:
                big_l = temp_l
                big_c = temp_c

            temp_c = char

        
        print(big_c*big_l, big_l)

    print(
        'Zad 4.3',
        *min(
            [[l, s] for l, s in pary if l == len(s)]
        )
    )