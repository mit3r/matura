

def listPrimes(n):

    if n < 2:
        return []

    sieve = [True] * (n + 1)

    i = 2

    while i*i <= n:
        if sieve[i]:
            j = i * i
            while j <= n:
                sieve[j] = False
                j += i

        i += 1
    
    return sieve


if __name__ == '__main__':

    liczby = [int(line.strip()) for line in open('czerw2022/przyklad.txt')]
    odbicia = list(map(lambda x: int(str(x)[-1::-1]), liczby))

    pod17 = list(filter(lambda x: x % 17 == 0, odbicia))

    print('Zad 4.1', pod17)

    maks_amp = 0
    maks_n = 0
    for i in range(len(liczby)):

        amp = abs(liczby[i] - odbicia[i])

        if amp > maks_amp:
            maks_amp = amp
            maks_n = liczby[i]

    print('Zad. 4.2', maks_n, maks_amp)

    primes = listPrimes(max(liczby))

    liczby_pierwsze = list(filter(lambda x: primes[x], liczby))

    odbicia_pierwsze = list(filter(lambda x: primes[int(str(x)[-1::-1])], liczby_pierwsze))

    print('Zad 4.3', odbicia_pierwsze)


    unikalne = set(liczby)

    count_rep = {u: 0 for u in list(unikalne)}

    for liczba in liczby:
        count_rep[liczba] += 1


    rep = [0, 0]
    for count in count_rep.values():

        if count > 3 or count == 0 or count == 1:
            continue

        rep[count-2] += 1

    print('Zad. 4.4 ', len(unikalne), rep)

    
