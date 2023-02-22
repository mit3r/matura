
def z(n): print(f'Zad 6.{n}')

if __name__ == '__main__':

    dane = [line.strip() for line in open('cyfra_kodkreskowy.txt', 'r')]
    dane = [line.split('\t') for line in dane[1:]]

    cyfry = { int(cyfra): kod for cyfra, kod, in dane }

    start = '11011010'
    stop = '11010110'

    kody = [int(line.strip()) for line in open('kody.txt', 'r')]

    z(1)

    sumy = []
    for i, liczba in enumerate(kody):

        sumy_even = sum([int(str(liczba)[n]) for n in range(len(str(liczba))-1, -1, -2)])
        sumy_odd = sum([int(str(liczba)[n]) for n in range(len(str(liczba))-2, -1, -2)])

        sumy += [[sumy_even, sumy_odd]]
    print(sumy)

    z(2)
    kontrolne = []
    for i, liczba in enumerate(kody):

        even, odd = sumy[i]

        kontroll = (10 - ((even * 3 + odd ) % 10)) % 10

        kontrolne += [kontroll]

        
    z(3)

    for i, liczba in enumerate(kody):
        kod = start + ''.join([cyfry[int(n)] for n in str(liczba)]) + str(kontrolne[i]) + stop
        print(kod)
        

    


