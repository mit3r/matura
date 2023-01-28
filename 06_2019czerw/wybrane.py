

def w(N: int):
    return sum(map(int, str(N)))

def wagaOf(n):

    while n >= 10:
        n = w(n)

    
    return n


def sitoera(n):

    sito  = [True for i in range(n+1)]
    sito[0] = False
    sito[1] = False

    for i in range(2, n+1):

        if sito[i]:
            j = i
            while j + i < n + 1:
                j += i
                sito[j] = False

    return sito




if __name__ == '__main__':

    sito = sitoera(4_300_000)
    print('sito dlugie na:', len(sito))

    liczby = [int(line.strip()) for line in open('./liczby.txt')]
    pierwsze = [int(line.strip()) for line in open('./pierwsze.txt')]

    print('liczby:', max(liczby), 'pierwsze:', max(pierwsze))


    print('Zad 4.1')

    odp = [liczba for liczba in liczby if 100 <= liczba <= 5000 and sito[liczba]]
    print(odp)

    print('Zad 4.2')

    odp = [pierwsza for pierwsza in pierwsze if sito[int(str(pierwsza)[::-1])]]
    print(odp)

    print('Zad 4.3')

    odp = len([pierwsza for pierwsza in pierwsze if wagaOf(pierwsza) == 1])
    print(odp)




