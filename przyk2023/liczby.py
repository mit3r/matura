

def wyznacz_b(M, a, x):
    return pow(a,x) % M

def wyznacz_x(M, a, b):
    x = 0

    while b != wyznacz_b(M, a, x):
        x += 1

    return x


def listPrimes(maks):
    
    lista = [True]*(maks+1)
    lista[0] = False
    lista[1] = False

    i = 2
    while i <= maks:

        if lista[i] == True:
            j = i + i
            while j <= maks:
                lista[j] = False
                j += i
        i += 1

    return lista

def dzielniki(n: int):

    dziel = set()
    for i in range(1, n+1):
        if n % i == 0:
            dziel.add(i)
            
        i += 1

    return dziel
    

if __name__ == '__main__':

    liczby = [[int(x) for x in line.strip().split()] for line in open('liczby_przyklad.txt')]


    maksimum = max([max(wiersz) for wiersz in liczby])
    primes = listPrimes(maksimum)

    ile_pierwszy = 0
    for wiersz in liczby:
        if primes[wiersz[0]]:
            ile_pierwszy += 1

    print('Zad 3.3', ile_pierwszy)

    relative_primes = 0
    for wiersz in liczby:

        n1 = wiersz[0]
        n2 = wiersz[1]

        wsp = list(dzielniki(n1).intersection(dzielniki(n2)))

        if len(wsp) == 1 and wsp[0] == 1:
            relative_primes += 1

    print('Zad 3.4', relative_primes)

    